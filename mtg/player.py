from . import errors, enums
from .card import Card, CustomCard
import random
import json
import pygame
import math
import time


class Player:
    def __init__(self, name, size=[1280, 720], **kwargs):
        self.name = name
        self.cards = []
        self.life = 20
        self.description = ""
        self.hand = []
        self.size = size
        self.card_back = pygame.transform.smoothscale(pygame.image.load("mtg/card_back.jpg"), (63, 88))  # TODO
        self.graveyard = []
        for k, v in kwargs.items():
            setattr(self, k, v)

    def add_card(self, card: Card):
        if not isinstance(card, Card):
            raise errors.NotCard("{!r} is not a subclass of Card".format(card))
        self.cards.append(card)

    def remove_card(self, name: str):
        for i, card in enumerate(self.cards):
            if card.name == name:
                return self.cards.pop(i)

    def start(self):
        random.shuffle(self.cards)
        for _ in range(7):
            self.draw_from_deck()

        while True:
            self.main.update()
            time.sleep(0.05)

    def draw_from_deck(self):
        print("draw")
        try:
            card = self.cards.pop()
            self.hand.append(card)

        except IndexError:
            self.deck_empty()

    def deck_empty(self):
        print("deck empty")

    def from_json(self, filename):
        with open(filename) as f:
            data = json.load(f)
            self.name = data["metadata"]["deckname"]
            self.description = data["metadata"].get("description", "")
            for amount, card_name in data["cards"].items():
                card = Card(card_name)
                for _ in range(amount):
                    self.add_card(card)
            for amount, custom_card in data.get("custom cards", []):
                name = dict.pop("name")
                custom_card["rarity"] = getattr(enums.Rarity, custom_card.get("rarity", "common"))
                custom_card["border"] = getattr(enums.Border, custom_card.get("border", "white"))
                custom_card["type"] = [getattr(enums.CardType, type) for type in custom_card.get("type", [])]

                card = CustomCard(name, **custom_card)


class CommanderPlayer(Player):
    def __init__(self, name, **kwargs):
        self.commander_card = None
        kwargs["life"] = kwargs.get("life", 40)
        super().__init__(name, **kwargs)

    @property
    def commander(self):
        return self.commander_card

    @commander.setter
    def commander_setter(self, other: Card):
        if not isinstance(other, Card):
            e = errors.NotCard("{!r} is not a subclass of Card".format(other))
            raise e
        if enums.SuperTypes.legendary not in other.supertypes:
            raise errors.NotLegendary("{!r} is not legendary".format(other))
        self.commander_card = other
