from film import Film

class FilmDVD(Film):
    def __init__(self, type):
        """initialise le type"""
        super().__init__()
        self.type = type