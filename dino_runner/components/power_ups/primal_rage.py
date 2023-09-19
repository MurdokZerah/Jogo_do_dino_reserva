from dino_runner.utils.constants import PRIMAL, PRIMAL_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Primal(PowerUp):
    def __init__(self):
        self.image = PRIMAL
        self.type = PRIMAL_TYPE
        super().__init__(self.image, self.type)
        