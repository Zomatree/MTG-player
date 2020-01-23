from enum import Enum, auto


class Borders(Enum):
    white = auto()
    blue = auto()
    black = auto()
    red = auto()
    green = auto()
    artifact = auto()
    gold = auto()


class Rarity(Enum):
    common = auto()
    uncommon = auto()
    rare = auto()
    mythic = auto()
