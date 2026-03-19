"""Module providing an implementation of a dog"""
from typing import Optional
import random

# Définition de l'exception personnalisée MatingError
class MatingError(Exception):
    """Exception levée lorsque deux chiens de même sexe tentent de s'accoupler."""
    pass


class Dog:
    """
    Une classe représentant un chien.

    Attributes:
        _race (str): La race du chien (protected).
        _sex (str): Le sexe du chien (protected).
        name (str): Le nom du chien (public).
    """

    def __init__(self, race: str, sex: str, name: str = "") -> None:
        """
        Initialise un chien avec une race, un sexe et un nom.

        Args:
            race (str): La race du chien.
            sex (str): Le sexe du chien ('M' ou 'F').
            name (str, optional): Le nom du chien. Par défaut, une chaîne vide.
        """
        self._race = race  # Attribut protégé pour la race
        self._sex = sex    # Attribut protégé pour le sexe
        self.name = name   # Attribut public pour le nom
        self._mother = None
        self._father = None
        self._puppies = []


    @property
    def race(self) -> str:
        """
        Retourne la race du chien.

        Returns:
            str: La race du chien.
        """
        return self._race

    @property
    def sex(self) -> str:
        """
        Retourne le sexe du chien.

        Returns:
            str: Le sexe du chien ('M' ou 'F').
        """
        return self._sex

    def bark(self, n=1):
        return "Woff"*n
    
    def chew(self, os):
        print(os[:-1])
    
    @property
    def mother(self) -> Optional['Dog']:
        """
        Retourne la mère du chien ou None.

        Returns:
            Optional[Dog]: La mère du chien ou None.
        """
        

    def mate(self, other: 'Dog') -> 'Dog':
        """
        Fait s'accoupler deux chiens et retourne un chiot.

        Args:
            other (Dog): L'autre chien avec lequel s'accoupler.

        Returns:
            Dog: Le chiot issu de l'accouplement.

        Raises:
            MatingError: Si les deux chiens sont de même sexe.
        """

        if self._sex == other._sex:
            raise MatingError("Pas possible, les chiens sont du même sexe")
        else:
            if self._sex == "M":
                pere = self
                mere = other
            else: 
                pere = other 
                mere = self
            if self._race == other._race:
                race = self._race
            else:
                race = "Bâtard"
            sexe = random.choice(["M", "F"])
            chiot = Dog(race,sexe)
            chiot._mother = mere
            chiot._father = pere
            pere._puppies.append(chiot)
            mere._puppies.append(chiot)
            return chiot
        

            



            # Vérification des sexes
            # Détermination du père et de la mère
            # Détermination de la race du chiot
            # Détermination du sexe du chiot (aléatoire)
            # Création du chiot
            # Assignation des parents
            # Ajout du chiot à la liste des chiots des parents


    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du chien.

        Returns:
            str: Une chaîne de caractères décrivant le chien.
        """
        return f"Chien: {self.name}, Race: {self._race}, Sexe: {self._sex}"

if __name__ == "__main__":
    pass