from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}:
            return f"{diver_type} is not allowed in our competition."

        existing_name = next((r for r in self.divers if r.name == diver_name), None)
        if existing_name:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        existing_name = next((r for r in self.fish_list if r.name == fish_name), None)
        if existing_name:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        # проверявам за съществуващ водолаз
        diver = next((diver for diver in self.divers if diver.name == diver_name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        # проверявам за същестуваща риба
        fish = next((fish for fish in self.fish_list if fish.name == fish_name), None)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        # проверявам за наличние на здравословен проблем
        if diver.has_health_issue:
            diver.update_health_status()
            if diver.has_health_issue:
                return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        recovered_divers = [diver for diver in self.divers if diver.has_health_issue]

        for diver in recovered_divers:
            diver.has_health_issue = False
            diver.renew_oxy()

        count = len(recovered_divers)
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = next((diver for diver in self.divers if diver.name == diver_name), None)

        if diver is None:
            return f"{diver_name} is not registered for the competition."

        catch_report = f"**{diver_name} Catch Report**\n"

        for fish in diver.catch:
            catch_report += f"{fish.fish_details()}\n"

        return catch_report

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]

        sorted_divers = sorted(healthy_divers,
                               key=lambda diver: (diver.competition_points, len(diver.catch), diver.name), reverse=True)

        statistics_report = "**Nautical Catch Challenge Statistics**\n"

        for diver in sorted_divers:
            statistics_report += f"{diver}\n"

        return statistics_report
