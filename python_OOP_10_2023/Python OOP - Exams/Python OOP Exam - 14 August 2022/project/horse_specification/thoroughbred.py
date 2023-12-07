from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)  # забравих super-а!!!

    def train(self):
        self.speed = min(self.speed + 3, 140)
