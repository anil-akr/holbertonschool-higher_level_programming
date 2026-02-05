#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite représentant un animal"""

    @abstractmethod
    def sound(self):
        """Méthode abstraite que chaque animal doit implémenter"""
        pass


class Dog(Animal):
    """Classe Dog qui hérite de Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Classe Cat qui hérite de Animal"""

    def sound(self):
        return "Meow"
