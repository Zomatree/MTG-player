import requests
from io import BytesIO
import enums
import errors

session = requests.Session()


class Card:
    def __init__(self, name):
        self.name = name
        get = session.get("https://api.magicthegathering.io/v1/cards?name=\"{}\"".format(name))
        if get.status_code != 200:
            raise errors.ImageRequestFailed("Failed to get image for card {}".format(name))
        self.json = get.json()["cards"][0]
        self.image_file = BytesIO(session.get(self.json["imageUrl"]).read())
        self.image_file.seek(0)

    def get_image(self):
        self.image_file.seek(0)
        return self.image_file


class CustomCard(Card):
    def __init__(self, name, *, cost=None, image,
                 border: enums.Borders = enums.Borders.white,
                 rarity: enums.Rarity = enums.Rarity.common,
                 card_type: enums.CardType = enums.CardType.creature):
        ...


"""
params for customcard:
- name
- cost:
   {5} - misc
   {W} - white
   {U} - blue
   {B} - black
   {R} - red
   {G} - green
- image:
    - https://image.url/here.png
    - "image.png"
- border:
    - Border
- rarity
- cardtype (cardtype enum)
- types (creature/artfact/etc)
- supertypes (legendary)
- subtypes (creature types - goblin/scout/etc)
- effect
- flavor
"""