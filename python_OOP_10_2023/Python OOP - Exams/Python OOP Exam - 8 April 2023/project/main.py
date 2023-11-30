from project.robots_managing_app import RobotsManagingApp

main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
# print(main_app.add_service('FashionService', 'ServiceFashionWorld'))

# женски роботи за SecondaryService - 2 броя
print(main_app.add_robot('FemaleRobot', 'Vania', 'HouseholdRobots', 100.00))
print(main_app.add_robot('FemaleRobot', 'Kalina', 'FunnyRobots', 200.00))

# женски роботи за SecondaryService - 2 броя
print(main_app.add_robot('MaleRobot', 'Gosho', 'TechRobots', 500.00))
print(main_app.add_robot('MaleRobot', 'Peter', 'TechRobots', 1000.00))

print(" --- add_robot_to_service ---")

# service - два женски робота - Ваня и Калина
print(main_app.add_robot_to_service('Vania', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Kalina', 'ServiceRobotsWorld'))

# роботи за работа - прав сценарий Петър
print(main_app.add_robot_to_service('Peter', 'ServiceTechnicalsWorld'))

# роботи за работа - грешен сценарий Гошо - Unsuitable service
print(main_app.add_robot_to_service('Gosho', 'ServiceRobotsWorld'))

# print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
# print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))
#
# принтирай общата цена на роботите
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))
#
# print(main_app.remove_robot_from_service('Kalina', 'ServiceRobotsWorld'))
# print(main_app.service_price('ServiceRobotsWorld'))
# print(main_app.service_price('ServiceTechnicalsWorld'))
#
# print(str(main_app))
