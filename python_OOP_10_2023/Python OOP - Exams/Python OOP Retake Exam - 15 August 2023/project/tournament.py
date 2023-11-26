from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        equipment = None
        valid_types = ["KneePad", "ElbowPad"]

        if equipment_type not in valid_types:
            raise Exception("Invalid equipment type!")

        if equipment_type == "KneePad":
            equipment = KneePad()
        elif equipment_type == "ElbowPad":
            equipment = ElbowPad()

        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country, advantage):
        team = None
        valid_types = ["OutdoorTeam", "IndoorTeam"]

        if team_type not in valid_types:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        # Проверка за уникалност на името на отбора
        if any(team.name == team_name for team in self.teams):
            return "Team name must be unique."

        if team_type == "OutdoorTeam":
            team = OutdoorTeam(team_name, country, advantage)
        elif team_type == "IndoorTeam":
            team = IndoorTeam(team_name, country, advantage)

        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        valid_types = ["KneePad", "ElbowPad"]

        if equipment_type not in valid_types:
            raise Exception("Invalid equipment type!")

        team = next((t for t in self.teams if t.name == team_name), None)

        if team is None:
            raise Exception(f"Team {team_name} does not exist.")

        equipment_to_sell = next((equip for equip in reversed(self.equipment) if type(equip).__name__ == equipment_type), None)

        if equipment_to_sell is None:
            raise Exception(f"No available {equipment_type} to sell.")

        # Проверка дали бюджетът на отбора е достатъчен за закупуване
        if team.budget < equipment_to_sell.price:
            raise Exception("Budget is not enough!")

        # Премахни оборудването от турнира и добави го към отбора
        self.equipment.remove(equipment_to_sell)
        team.equipment.append(equipment_to_sell)

        # Намали бюджета на отбора с цената на оборудването
        team.budget -= equipment_to_sell.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)

        if team is None:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        valid_types = ["KneePad", "ElbowPad"]

        if equipment_type not in valid_types:
            raise Exception("Invalid equipment type!")

        changed_equipment_count = 0

        for equip in self.equipment:
            if type(equip).__name__ == equipment_type:
                equip.increase_price()
                changed_equipment_count += 1

        return f"Successfully changed {changed_equipment_count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)

        if not isinstance(team1, type(team2)):
            raise Exception("Game cannot start! Team types mismatch!")

        advantage_and_protection1 = team1.advantage + sum(equip.protection for equip in team1.equipment)
        advantage_and_protection2 = team2.advantage + sum(equip.protection for equip in team2.equipment)

        if advantage_and_protection1 > advantage_and_protection2:
            team1.win()
            return f"The winner is {team_name1}."
        elif advantage_and_protection1 < advantage_and_protection2:
            team2.win()
            return f"The winner is {team_name2}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: x.wins, reverse=True)

        team_statistics = "\n".join([team.get_statistics() for team in sorted_teams])

        return f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n{team_statistics}"
