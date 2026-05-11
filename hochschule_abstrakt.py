from abc import ABC, abstractmethod

class Person(ABC):
    """  Abstrakte Klasse zur Repräsentation von Personen.
Die Methode reset_default() ist von den Subklassen zu implementieren """
    def __init__(self, name=None, geburtsjahr=None):
        self._name = name
        self._geburtsjahr = geburtsjahr

    def __str__(self):
        return f"Person: {self.name}, Geburtsjahr: {self.geburtsjahr}"

    @abstractmethod
    def reset_default_values(self):
        pass


class Studierender(Person):
    """ Klass Studierender als Spezialisierung von Person """
    def __init__(self, name=None, geburtsjahr=None, matrNR=None):
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
        """ Zurücksetzen der Attribute auf Standardwerte """
        self.name = "Standard-Studierender"
        self.geburtsjahr = None
        self.matrNr = None



class Dozent(Person):
    """ Klasse Dozent als Spezialisierung von Person """
    def __init__(self, name, geburtsjahr):
        super().__init__(name=name, geburtsjahr=geburtsjahr, besGr=None )
        self._besGr = besGr

    @property
    def besoldungsgruppe(self):
        return self._besoldungsgruppe
    
    @besoldungsgruppe.setter
    def besoldungsgruppe(self, value):
        self._besoldungsgruppe = value

    def __str__(self):
        return f"{super().__str__()} und gleichzeitig Dozent mit Besoldungsgruppe {self.besoldungsgruppe}"

    def reset_default_values(self):
        """ Zurücksetzen der Attribute auf Standardwerte """
        self.name = "Standard-Dozent"
        self.geburtsjahr = 1900
        self.besoldungsgruppe = None


class Angestellter():
    """ Klasse zur Repräsentation von Angestellten """
    def __init__(self, vetragsjahr=None):
        self._vertragsjahr = vetragsjahr

    def verlaengern(self):
        """ verlängert den Vertag um ein Jahr """
        self._vertragsjahr += 1
    
    def __str__(self):
        return f"Angestellter bis {self._vertragsjahr}"
    
    def drucken(self):
        print(self)

class Dozent2(Person, Angestellter):
    """ Klasse Dozent als Spezialisierung von Person """
    def __init__(self, name=None, geburtsjahr=None, vertragsjahr=None, besoldungsgruppe=None):
        Person.__init__(self, name=name, geburtsjahr=geburtsjahr)
        Angestellter.__init__(self, vertragsjahr=vertragsjahr)
        self._besoldungsgruppe = besoldungsgruppe
    def __str__(self):
        return f"{Person.__str__(self)}, {Angestellter.__str__(self)} " \
        f"und gleichzeitig Dozent mit Besoldungsgruppe {self._besoldungsgruppe}"
    




# ============= Daten Einfügen =============
s2 = Studierender(name="Petra", geburtsjahr=1999, matrNr=123457)
d1 = Dozent(name="Hans", geburtsjahr=1984, besoldungsgruppe="W2")
p1 = Person(name="Julia", geburtsjahr=2001)
personen_liste = [s2, p1, d1]

for p in personen_liste:
    print(type(p))
    p.drucken()