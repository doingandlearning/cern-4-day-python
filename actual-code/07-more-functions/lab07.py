players = {'Player1': 0,
           'Player2': 2,
           'Player3': 2,
           'Player4': 0,
           'Player5': 1,
           'Player6': 1,
           'Player7': 3,
           'Player8': 4,
           'Player9': 4,
           'Player10': 0
           }

# Who scored more than 2 points?
print(list(filter(lambda player: players[player] > 2, players)))
# Sort the players by score
print(sorted(players.items(), key=lambda player: player[1], reverse=True))
# What are the total points scored by all players?
print(sum(players.values()))
# Who scored exactly 4 points?
# How many players scored more than 1 point?
# Wha are the scores as a percentage of the maximum?
# What is the average score?


