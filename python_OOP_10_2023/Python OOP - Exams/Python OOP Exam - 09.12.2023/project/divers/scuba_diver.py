from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch: int):
        oxygen_reduction = round(time_to_catch * 0.60)

        if self.oxygen_level >= oxygen_reduction:
            self.oxygen_level -= oxygen_reduction
        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = 540
