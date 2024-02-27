players = ['kim', 'hong', 'choi', 'park', 'jo', 'lee']
print(players[1:4])
print(players[-4:])

print("Here are the first three players on my team")
for player in players[:3]:
    print("Good Job, " + player.title())