from . import Card, NotCard


class Player:
    def __init__(self, name, **kwargs):
        self.name = name
        self.cards = []
        self.life = 20
        for k, v in kwargs.items():
            setattr(self, k, v)

    def add_card(self, card: Card):
        if not isinstance(card, Card):
            raise NotCard("{!r} is not a subclass of Card".format(card))
        self.cards.append(card)

    def remove_card(self, name: str):
        for i, card in enumerate(self.cards):
            if card.name == name:
                return self.cards.pop(i)

    def start(self):
        NotImplemented  # TODO


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
            raise NotCard("{!r} is not a subclass of Card".format(other))
        self.commander_card = other
