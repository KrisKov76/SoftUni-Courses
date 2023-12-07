from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0
    MEAL_TYPES = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.client = None
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        # 1. намираме клиента през генератор с първо съвпадение
        existing_client = next((r for r in self.clients_list if r.phone_number == client_phone_number), None)

        # 2. ако има съществуващ клиент - вече е регистриран!
        if existing_client:
            raise Exception("The client has already been registered!")
        # 3. създаваме нов клиент
        new_client = Client(client_phone_number)  # създай клиент с този телефонен номер
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if type(meal).__name__ in self.MEAL_TYPES:  # ако името на класа съвпада...
                self.menu.append(meal)  # добави го в menu

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')
        menu_details = [meal.details() for meal in self.menu]
        return '\n'.join(menu_details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        meals_to_order = []
        current_bill = 0
        client = next((r for r in self.clients_list if r.phone_number == client_phone_number), None)

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            matching_meals = [meal for meal in self.menu if meal.name == meal_name]  # съответстващи ястия
            try:
                selected_meal = next(meal for meal in matching_meals if meal.quantity >= meal_quantity)
                meals_to_order.append(selected_meal)
                current_bill += selected_meal.price * meal_quantity
            except StopIteration:
                raise Exception(f"Not enough quantity of {type(self.menu[0]).__name__}: {meal_name}!")
            except IndexError:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next((client for client in self.clients_list if client.phone_number == client_phone_number), None)
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}
        return f"Client {client_phone_number} successfully canceled his order."


    def finish_order(self, client_phone_number):
        client = next((client for client in self.clients_list if client.phone_number == client_phone_number), None)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
