from mtg import Card, Player, CustomCard, CardType, Border, Rarity

player = Player.commander("Golos")
player.set_commander(Card("Golos, Tireless Pilgrim"))

player.from_json("cards.json")
# or
player.add_card(Card("Name Here"))  # real card name, will attempt to fetch the image of it
player.add_card(CustomCard(
    "You win the game card",
    cost="{5}{W}{U}{B}{R}{G}",
    image="https://image.url/here.png" or "winthegame.png",
    border=Border.white,
    rarity=Rarity.mythic,
    type=CardType.instant,
    effect="if you have less that 1 life you win the game",
    flavor="Even in the worst of place there is still hope"))

player.add_card(CustomCard(
    "sparker",
    cost="3c",
    image="https://image.url/here.png" or "sparker.png",
    border=Border.artifact,
    rarity=Rarity.uncommon,
    type=CardType.artifact,
    effect="[[tap]][white]]deal one damage to any target",
    flavor="Even in the worst of place there is still hope"))

player.start()

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
