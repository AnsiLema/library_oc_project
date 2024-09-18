from abc import ABC, abstractmethod

"""Création de l'objet Film"""


class Film(ABC):
    def __init__(self, name, created_in, place):
        """initialisation des attributs de Film"""
        self.name = name
        self.created_in = created_in
        self.place = place
