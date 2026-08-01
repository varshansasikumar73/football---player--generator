import random
players = [{"name": "Messi", "rating": 99}, {"name": "Ronaldo", "rating": 97}, {"name": "Neymar", "rating": 96}, {"name": "Mbappe", "rating": 98}, {"name": "Olise", "rating": 94}, {"name": "Lamine Yamal", "rating": 95}, {"name": "Haaland", "rating": 96}, {"name": "Jude Bellingham", "rating": 96}, {"name": "Harry Kane", "rating": 92}, {"name": "Djed Spence", "rating": 83}, {"name": "Stiff Bucko", "rating": 100}, {"name": "Kevin De Bruyne", "rating": 90}, {"name": "Dembele", "rating": 93}]
name_ofplayer1 = input("Enter the name of player 1:")
name_ofplayer2 = input("Enter the name of player 2:")
player_1 = random.choice(players)
players.remove(player_1)
player_2 = random.choice(players)
print(name_ofplayer1 + ":selected " + player_1["name"], "with a rating of", str(player_1["rating"]))
print(name_ofplayer2 + ":selected " + player_2["name"], "with a rating of", str(player_2["rating"]))
if player_1["rating"] > player_2["rating"]:
    print(name_ofplayer1 + " wins with " + player_1["name"])
elif player_1["rating"] < player_2["rating"]:
    print(name_ofplayer2 + " wins with " + player_2["name"])
else:
    print("It's a tie between " + name_ofplayer1 + " and " + name_ofplayer2)

          




