def add_songs(*args):
    collection = {}

    for song_name, lyrics in args:
        if song_name not in collection:
            collection[song_name] = []
        collection[song_name] += lyrics

    result = ''

    for name, lyrics in collection.items():
        result += f"- {name}\n"
        if lyrics:
            result += '\n'.join(lyrics) + '\n'
    return result
