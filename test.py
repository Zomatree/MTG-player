import mtg

player = mtg.Player("test")

player.add_card(mtg.Card("island"))
player.add_card(mtg.Card("forest"))
player.add_card(mtg.Card("mountain"))
player.add_card(mtg.Card("plains"))
player.add_card(mtg.Card("swamp"))
player.add_card(mtg.Card("swarm intelligence"))
player.add_card(mtg.Card("heartstone"))
player.add_card(mtg.Card("essence scatter"))
player.add_card(mtg.Card("duneblast"))
player.add_card(mtg.Card("winds of abandon"))

player.start()
