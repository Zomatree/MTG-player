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


class CardType(Enum):
    creature = auto()
    land = auto()
    artifact = auto()
    enchantment = auto()
    sorcery = auto()
    planeswalker = auto()
    instant = auto()


class SuperTypes(Enum):
    basic = auto()
    legendary = auto()
    snow = auto()


class ButtonType(Enum):
    rect = 1
    polygon = 2
    circle = 3
    ellipse = 4
    image = 5
