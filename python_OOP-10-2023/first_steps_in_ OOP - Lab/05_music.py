class Music:
    def __init__(self, title: str, artist: str, lyrics: str):  # lyrics: str - анотации
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self) -> str:  # -> str анотация, че ще връща string
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


# вдигнахме си инстанцията song1
song1 = Music("Godzilla", "Eminem", "i can swallow a bottle of")
print(song1.print_info())
print(song1.play())
