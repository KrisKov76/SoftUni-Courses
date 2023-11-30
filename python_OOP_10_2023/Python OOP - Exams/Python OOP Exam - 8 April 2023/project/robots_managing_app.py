from project.roboti.female_robot import FemaleRobot
from project.roboti.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots_serv = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")
        self.services.append(self.SERVICE_TYPES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        self.robots_serv.append(self.ROBOT_TYPES[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

        # if robot_type == "MaleRobot":
        #     robot = MaleRobot(name, kind, price)
        # elif robot_type == "FemaleRobot":
        #     robot = FemaleRobot(name, kind, price)
        # else:
        #     raise Exception("Invalid robot type!")
        # self.robots_serv.append(robot)
        # return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot_obj = [obj for obj in self.robots_serv if obj.name == robot_name][0]
        service_obj = [obj for obj in self.services if obj.name == service_name][0]

        if robot_obj.POSSIBLE_SERVICE != service_obj.__class__.__name__:
            return "Unsuitable service."
        if len(service_obj.robo_lst) >= service_obj.capacity:
            raise Exception("Not enough capacity for this robot!")
        self.robots_serv.remove(robot_obj)
        service_obj.robo_lst.append(robot_obj)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service_obj = [obj for obj in self.services if obj.name == service_name][0]  # secondary_service
        robot = [r for r in service_obj.robo_lst if r.name == robot_name]

        print(service_obj, robot)

        if not robot:
            raise Exception("No such robot in this service!")
        robot_obj = robot[0]
        service_obj.robo_lst.remove(robot_obj)  # премахни от secondaryService
        self.robots_serv.append(robot_obj)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service_obj = [obj for obj in self.services if obj.name == service_name][0]
        [r.eating() for r in service_obj.robo_lst]
        return f"Robots fed: {len(service_obj.robo_lst)}."

    # Каква е общата цена на роботите, включени в service-a по service_name ?
    def service_price(self, service_name: str):
        service_obj = [obj for obj in self.services if obj.name == service_name][0]
        total_price = sum([r.price for r in service_obj.robo_lst])
        return f"The value of service {service_name} is {total_price:.2f}."

    #
    def __str__(self):
        return '\n'.join([s.details() for s in self.services])
