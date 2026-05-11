from abc import ABC, abstractmethod

class Person(ABC):
    """ Abstrakte Klasse zur Repräsentation von Personen.
        Die Methode reset_default() ist von den Subklassen zu implementieren """
    def __init__(self, name=None, geburtsjahr=None):
        self._name = name
        self._geburtsjahr = geburtsjahr

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def geburtsjahr(self):
        return self._geburtsjahr

    @geburtsjahr.setter
    def geburtsjahr(self, value):
        self._geburtsjahr = value

    def __str__(self):
        return f"Person: {self.name}, Geburtsjahr: {self.geburtsjahr}"

    @abstractmethod
    def reset_default_values(self):
        pass


class Studierender(Person):
    """ Klasse Studierender als Spezialisierung von Person """
    def __init__(self, name=None, geburtsjahr=None, matrNr=None):
        super().__init__(name=name, geburtsjahr=geburtsjahr)
        self._matrNr = matrNr

    @property
    def matrNr(self):
        return self._matrNr

    @matrNr.setter
    def matrNr(self, value):
        self._matrNr = value

    def __str__(self):
        return f"{super().__str__()} und gleichzeitig Studierender mit Matrikelnummer {self.matrNr}"

    def reset_default_values(self):
        self.name = "Standard-Studierender"
        self.geburtsjahr = None
        self.matrNr = None


class Dozent(Person):
    """ Klasse Dozent als Spezialisierung von Person """
    def __init__(self, name=None, geburtsjahr=None, besoldungsgruppe=None):
        super().__init__(name=name, geburtsjahr=geburtsjahr)
        self._besoldungsgruppe = besoldungsgruppe

    @property
    def besoldungsgruppe(self):
        return self._besoldungsgruppe
    
    @besoldungsgruppe.setter
    def besoldungsgruppe(self, value):
        self._besoldungsgruppe = value

    def __str__(self):
        return f"{super().__str__()} und gleichzeitig Dozent mit Besoldungsgruppe {self.besoldungsgruppe}"

    def reset_default_values(self):
        self.name = "Standard-Dozent"
        self.geburtsjahr = 1900
        self.besoldungsgruppe = None


# Добавляем метод drucken ко всем
Person.drucken = lambda self: print(self)
Studierender.drucken = lambda self: print(self)
Dozent.drucken = lambda self: print(self)


# Тестирование
s2 = Studierender(name="Petra", geburtsjahr=1999, matrNr=123457)
d1 = Dozent(name="Hans", geburtsjahr=1984, besoldungsgruppe="W2")

personen_liste = [s2, d1]

for p in personen_liste:
    print(type(p))
    p.drucken()