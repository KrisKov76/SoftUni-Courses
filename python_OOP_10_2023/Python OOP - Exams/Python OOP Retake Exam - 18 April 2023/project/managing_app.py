from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        # Проверка дали вече съществува потребител със същия номер
        existing_user = next((user for user in self.users if user.driving_license_number == driving_license_number),
                             None)
        if existing_user:
            return f"{driving_license_number} has already been registered to our platform."
        else:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        existing_vehicle = next((vehicle for vehicle in self.vehicles
                                 if vehicle.license_plate_number == license_plate_number), None)
        new_vehicle = None  # Инициализация на променливата

        if existing_vehicle:
            return f"{license_plate_number} belongs to another vehicle."
        else:
            if vehicle_type == "PassengerCar":
                new_vehicle = PassengerCar(brand, model, license_plate_number)
            elif vehicle_type == "CargoVan":
                new_vehicle = CargoVan(brand, model, license_plate_number)

            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point, end_point, length):
        existing_route = next((route for route in self.routes if route.start_point == start_point
                               and route.end_point == end_point), None)
        if existing_route:
            if existing_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if existing_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if existing_route.length > length:
                existing_route.is_locked = True

        route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened):
        user = next((user for user in self.users if user.driving_license_number == driving_license_number), None)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = next((vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number),
                       None)

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = next((route for route in self.routes if route.route_id == route_id), None)

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count):
        # Избиране само на повредени превозни средства
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]

        # Сортиране на избраните превозни средства по марка и след това по модел
        sorted_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))

        # Вземане на първите count превозни средства, или всички, ако count е по-голям от броя повред. превоз. средства
        selected_vehicles = sorted_vehicles[:count]

        # Ремонт и презареждане на избраните превозни средства
        for vehicle in selected_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100

        # Бройката на ремонтираните превозни средства
        count_of_repaired_vehicles = len(selected_vehicles)

        # Връщане на съобщение за успешно ремонтиране
        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***", ]
        sorted_users = sorted(self.users, key=lambda user: -user.rating)
        result.append(('\n'.join(str(user) for user in sorted_users)))
        return '\n'.join(result)



