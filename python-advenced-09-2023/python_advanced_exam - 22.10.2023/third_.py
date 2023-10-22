def team_lineup(*args):
    collection = {}

    for football_player, country in args:
        if country not in collection:
            collection[country] = []
        collection[country].append(football_player)

    sorted_list = sorted(collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''
    # Извеждане...
    for key, value in sorted_list:
        result += f"{key}:\n"
        for item in value:
            result += f"  -{item}\n"

    return result

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

