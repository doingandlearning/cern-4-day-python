player = {
    "Matthias": 1,
    "Bart": 4,
    "Sevgi": -1,
    "Albane": 2
}

# sorted_players = list(player.items())
# sorted_players.sort(key=lambda player:player[1])
#
# print(sorted_players)
print(sorted(player.items(), key=lambda player:player[1], reverse=True))
print(player.items())