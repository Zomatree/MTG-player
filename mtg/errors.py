class NotCard(Exception):
    """Not a subclass of mtg.Card"""


class ImageRequestFailed(Exception):
    """Getting the image for a card failed"""


class NotLegendary(Exception):
    """The Card is not legendary when it is required to be"""
