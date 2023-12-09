from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_horse(self, horse_type_):
        found = next((r for r in reversed(self.horses) if type(r).__name__ == horse_type_ and not r.is_taken), None)

        if not found:
            raise Exception(f"Horse breed {horse_type_} could not be found!")
        return found

    def find_jockey(self, jockey_name_):
        found = next((r for r in self.jockeys if r.name == jockey_name_), None)
        if not found:
            raise Exception(f"Jockey {jockey_name_} could not be found!")
        return found

    def find_horse_race(self, race_type_):
        found = next((r for r in self.horse_races if r.race_type == race_type_), None)
        if not found:
            raise Exception(f"Race {race_type_} could not be found!")
        return found

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_TYPES:
            return # това също е важно, защото реално казва - ако го няма там, да върне нищо
        existing_name = next((r for r in self.horses if r.name == horse_name), None)
        if existing_name:
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = self.VALID_TYPES[horse_type](horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        # existing_name = next((r for r in self.jockeys if r.name == jockey_name), None)
        existing_name = [r for r in self.jockeys if r.name == jockey_name]
        if existing_name:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)  # създавам нов обект Jockey
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(horse_race.race_type == race_type for horse_race in self.horse_races):  # не го съобразих!
            raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)  # creates a race
        self.horse_races.append(new_race) # adds it to the horse races
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey(jockey_name)
        horse = self.find_horse(horse_type)

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        else:
            jockey.horse = horse  # прикрепяме коня към жокея
            horse.is_taken = True  # конят е взет horse.is_taken
            return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.find_horse_race(race_type)
        jockey = self.find_jockey(jockey_name)

        if not jockey.horse:  # If the jockey is on the jockeys' list, but he/she doesn't have a horse
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:  # If the jockey has already been added to the horse race
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'
        else:
            race.jockeys.append(jockey)  # add the jockey (object) to the given horse race
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.find_horse_race(race_type)

        if len(race.jockeys) < 2:  # The participants in a horse race must be at least 2
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        the_fastest_jockey = sorted(race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]

        return f'The winner of the {race_type} race, with a speed of {the_fastest_jockey.horse.speed}km/h ' \
               f'is {the_fastest_jockey.name}! Winner\'s horse: {the_fastest_jockey.horse.name}.'
