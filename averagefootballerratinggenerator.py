import random
players = [{"name": "Messi", "rating": 99}, {"name": "Ronaldo", "rating": 97}, {"name": "Neymar", "rating": 96}, {"name": "Mbappe", "rating": 98}, {"name": "Olise", "rating": 94}, {"name": "Lamine Yamal", "rating": 95}, {"name": "Haaland", "rating": 96}, {"name": "Jude Bellingham", "rating": 96}, {"name": "Harry Kane", "rating": 92}, {"name": "Djed Spence", "rating": 83}, {"name": "Stiff Bucko", "rating": 100}, {"name": "Kevin De Bruyne", "rating": 90}, {"name": "Dembele", "rating": 93}, {"name": "Enzo Fernandez", "rating": 78}, {"name": "Bukayo Saka", "rating": 88}, {"name": "Phil Foden", "rating": 87}, {"name": "Vinicius Jr.", "rating": 89}, {"name": "Rodri", "rating": 86}, {"name": "Casemiro", "rating": 85}, {"name": "Frenkie de Jong", "rating": 84}, {"name": "Joshua Kimmich", "rating": 90}, {"name": "Trent Alexander-Arnold", "rating": 88}, {"name": "Alisson Becker", "rating": 89}, {"name": "Jan Oblak", "rating": 91}, {"name": "Sithole", "rating": 62}]
count = 0
playercount = 0
total = 0
selected_players = []
while count < 5:
    name_ofplayer1 = input(f"Enter the name of footballer {count + 1}: ")
    if name_ofplayer1 not in [player["name"] for player in players]:
        print("Player not found. Please enter a valid player name.")
        continue
    elif name_ofplayer1 in selected_players:
        print("Player already selected. Please choose a different player.")
        continue
    selected_players.append(name_ofplayer1)
    count += 1
for player in selected_players:
    for x in players:
        if player == x["name"]:
            total += x["rating"]
average = total/5
print(f"Your average player rating is: {average}")



        


    
