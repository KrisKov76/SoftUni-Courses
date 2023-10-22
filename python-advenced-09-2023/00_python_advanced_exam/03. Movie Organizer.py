def movie_organizer(*args):  # сбор от тюпъли
    collection = {}

    for movie_name, genre in args:  # разопаковаме тюпълите
        # слагаме си ги в dict, за да ни е по-удобно за сортировката
        if genre not in collection:
            collection[genre] = []
        collection[genre].append(movie_name)

    # сортираме - не забравяме .items(), (-len(kvp[1]) десцендинг от бройката в листа, kvp[0] - по ключовете
    sorted_movie_collection = sorted(collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''

    # принтираме, като разопаковаме сортирания речник
    for genre, movies in sorted_movie_collection:
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            result += f"* {movie}\n"
    return result