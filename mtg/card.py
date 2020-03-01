import requests
from io import BytesIO
from . import enums, errors
import typing
import re
import os


regex = r"^(\{([1-10]|W|U|B|R|G|S)\})+$"
session = requests.Session()


class Card:
    def __init__(self, name, base_url=None):
        self.name = name
        exists = os.path.exists(f"image_cache/{name}.png")
        if not exists:
            if not base_url:
                base_url = "https://api.magicthegathering.io/v1/cards?name=\"{}\""

            get = session.get(base_url.format(name))
            if get.status_code != 200:
                message = "Failed to get image for card {}".format(name)
                raise errors.ImageRequestFailed(message)

            self.json = get.json()["cards"][0]
            self.image_file = BytesIO(session.get(self.json["imageUrl"]).content)
            self.image_file.seek(0)
        else:
            self.image_file = open(f"image_cache/{name}.png")

        if not exists:
            with open(f"image_cache/{name}.png", "w+") as f:
                f.write(self.file_image)

    def get_image(self):
        return self.file_image

    def __repr__(self):
        if getattr(self, "json", None):
            type = self.json["type"]
        else:
            type = " "
        return "<{} name={} type={}>".format(type(self).__name__, self.name, type)


class CustomCard(Card):
    def __init__(self, name, *, cost=None, image,
                 border: enums.Borders = enums.Borders.white,
                 rarity: enums.Rarity = enums.Rarity.common,
                 card_types: typing.List[enums.CardType] = None,
                 supertypes: typing.List[enums.SuperTypes] = None,
                 # subtypes: typing.List[enums.SubTypes] = None,
                 effect: str = None, flavor: str = None):
        ...
