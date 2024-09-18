import random

class Library:
    def __init__(self):
        """Attribut d'instance initialisé en tant que liste vide"""
        self.films_list = []

    def add_film(self, film):
        self.films_list.append(film)

    def sort_by_date(self):
        self.films_list.sort(key= lambda film: film.created_in)

    def sort_by_name(self):
        self.films_list.sort(key= lambda film: film.name)

    def sort_by_type(self):
        self.films_list.sort(key= lambda film: film.type)

    def random_film(self):
        if self.films_list:
            return random.choice(self.films_list)
        else:
            return None