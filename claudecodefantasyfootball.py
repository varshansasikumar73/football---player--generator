import random

BUDGET = 500
SQUAD_SIZE = 5

PLAYERS = [
    {"name": "Messi", "rating": 99},
    {"name": "Ronaldo", "rating": 97},
    {"name": "Neymar", "rating": 96},
    {"name": "Mbappe", "rating": 98},
    {"name": "Olise", "rating": 94},
    {"name": "Lamine Yamal", "rating": 95},
    {"name": "Haaland", "rating": 96},
    {"name": "Jude Bellingham", "rating": 96},
    {"name": "Harry Kane", "rating": 92},
    {"name": "Djed Spence", "rating": 83},
    {"name": "Stiff Bucko", "rating": 100},
    {"name": "Kevin De Bruyne", "rating": 90},
    {"name": "Dembele", "rating": 93},
    {"name": "Enzo Fernandez", "rating": 78},
    {"name": "Bukayo Saka", "rating": 88},
    {"name": "Phil Foden", "rating": 87},
    {"name": "Vinicius Jr.", "rating": 89},
    {"name": "Rodri", "rating": 86},
    {"name": "Casemiro", "rating": 85},
    {"name": "Frenkie de Jong", "rating": 84},
    {"name": "Joshua Kimmich", "rating": 90},
    {"name": "Trent Alexander-Arnold", "rating": 88},
    {"name": "Alisson Becker", "rating": 89},
    {"name": "Jan Oblak", "rating": 91},
    {"name": "Sithole", "rating": 62},
]

for player in PLAYERS:
    player["cost"] = round(player["rating"] * 1.2)


def display_pool(pool):
    print(f"\n{'#':<3}{'Name':<24}{'Rating':<8}{'Cost':<6}")
    for i, player in enumerate(pool, start=1):
        print(f"{i:<3}{player['name']:<24}{player['rating']:<8}{player['cost']:<6}")


def find_player(pool, choice):
    choice = choice.strip()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(pool):
            return pool[index]
        return None
    for player in pool:
        if player["name"].lower() == choice.lower():
            return player
    return None


def user_draft(pool):
    squad = []
    budget_left = BUDGET
    print(f"\nYou have £{BUDGET}m to build a squad of {SQUAD_SIZE} players.")
    while len(squad) < SQUAD_SIZE:
        if all(player["cost"] > budget_left for player in pool):
            print(f"\nYou've gone bust! £{budget_left}m left isn't enough to afford anyone else.")
            return squad, True
        display_pool(pool)
        print(f"\nBudget remaining: £{budget_left}m | Players picked: {len(squad)}/{SQUAD_SIZE}")
        choice = input("Pick a player (name or number): ")
        player = find_player(pool, choice)
        if player is None:
            print("Player not found. Try again.")
            continue
        if player["cost"] > budget_left:
            print(f"Too expensive! {player['name']} costs £{player['cost']}m, you have £{budget_left}m left.")
            continue
        squad.append(player)
        budget_left -= player["cost"]
        pool.remove(player)
    return squad, False


def ai_draft(pool):
    squad = []
    budget_left = BUDGET
    candidates = pool.copy()
    random.shuffle(candidates)
    while len(squad) < SQUAD_SIZE and candidates:
        slots_after = SQUAD_SIZE - len(squad) - 1
        picked = None
        for player in candidates:
            if player["cost"] > budget_left:
                continue
            others = sorted((p for p in candidates if p is not player), key=lambda p: p["cost"])
            if len(others) < slots_after:
                continue
            reserve = sum(p["cost"] for p in others[:slots_after])
            if player["cost"] + reserve <= budget_left:
                picked = player
                break
        if picked is None:
            break
        squad.append(picked)
        budget_left -= picked["cost"]
        candidates.remove(picked)
    return squad


def average_rating(squad):
    return sum(p["rating"] for p in squad) / len(squad)


def print_squad(title, squad):
    print(f"\n{title}")
    for player in squad:
        print(f"  {player['name']} (rating {player['rating']}, cost £{player['cost']}m)")
    print(f"  Average rating: {average_rating(squad):.1f}")


def play_round():
    user_squad, went_bust = user_draft([p.copy() for p in PLAYERS])
    ai_squad = ai_draft([p.copy() for p in PLAYERS])

    print_squad(f"Your squad ({len(user_squad)}/{SQUAD_SIZE}):", user_squad)
    print_squad("AI's squad:", ai_squad)

    if went_bust:
        print(f"\nAI wins by default - you went bust with only {len(user_squad)} players.")
        return

    user_avg = average_rating(user_squad)
    ai_avg = average_rating(ai_squad)

    print()
    if user_avg > ai_avg:
        print(f"You win! {user_avg:.1f} vs {ai_avg:.1f}")
    elif ai_avg > user_avg:
        print(f"AI wins. {ai_avg:.1f} vs {user_avg:.1f}")
    else:
        print(f"It's a draw. {user_avg:.1f} vs {ai_avg:.1f}")


def main():
    print("=== Fantasy Draft ===")
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
