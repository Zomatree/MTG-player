class NotCard(Exception):
    """Not a subclass of mtg.Card"""


class ImageRequestFailed(Exception):
    """Getting the image for a card failed"
