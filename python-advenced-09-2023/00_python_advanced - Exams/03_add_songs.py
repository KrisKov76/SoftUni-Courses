def add_songs(*args):
    collection = {}

    for song_name, lyrics in args:
        if song_name not in collection:
            collection[song_name] = []
        collection[song_name] += lyrics

    result = ''

    for name, lyrics in collection.items():
        result += f"- {name}\n"
        result += '\n'.join(lyrics) + '\n'
    return result

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))

# 90.0 %