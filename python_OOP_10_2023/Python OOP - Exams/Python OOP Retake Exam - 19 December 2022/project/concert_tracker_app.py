from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []
        self.active = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIAN_TYPES:
            raise ValueError('Invalid musician type!')
        self.musicians.append(self.MUSICIAN_TYPES[musician_type](name, age))
        return f'{name} is now a {musician_type}.'

    def create_band(self, name: str):
        if name in self.bands:
            raise Exception(f"{name} band is already created!")
        band = Band(name)  # вдигам инстанция band
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for r in self.concerts:
            if r.place == place:
                raise ValueError(f"{place} is already registered for {r.genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)  # вдигам инстанция concert
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        existing_musician = next((r for r in self.musicians if r.name == musician_name), None)
        if not existing_musician:
            raise Exception(f"{musician_name} isn't a musician!")
        existing_band = next((r for r in self.bands if r.name == band_name), None)
        if not existing_band:
            raise Exception(f"{band_name} isn't a band!")
        existing_band.members.append(musician_name)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in self.bands:
            raise Exception(f"{band_name} isn't a band!")
        existing_band = next((r for r in self.bands if r.name == band_name), None)
        existing_musician_in_band = next((r for r in existing_band.members if r.name == musician_name), None)

        if not existing_musician_in_band:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        existing_band.members.remove(musician_name)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        concert = next((r for r in self.concerts if r.place == concert_place), None)

        singer_found = (isinstance(member, Singer) for member in band.members)
        drummer_found = (isinstance(member, Drummer) for member in band.members)
        guitarist_found = (isinstance(member, Guitarist) for member in band.members)

        if not(singer_found and drummer_found and guitarist_found):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

