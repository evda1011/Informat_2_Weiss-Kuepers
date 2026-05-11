class Person:
    """ Klasse zur Repräsentation von Personen """
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

    def drucken(self):
        print(self)


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


class Angestellter:
    """  Klasse zur Repräsentation von Angestellten  """
    def __init__(self, vertragsjahr=None):
        self._vertragsjahr = vertragsjahr

    def verlaengern(self):
        """ Продлить контракт на год """
        if self._vertragsjahr is not None:
            self._vertragsjahr += 1

    def __str__(self):
        return f"Angestellter bis {self._vertragsjahr}"

    def drucken(self):
        print(self)


class Dozent2(Person, Angestellter):
    """ Dozent + Angestellter (множественное наследование) """
    def __init__(self, name=None, geburtsjahr=None, vertragsjahr=None, besoldungsgruppe=None):
        Person.__init__(self, name=name, geburtsjahr=geburtsjahr)
        Angestellter.__init__(self, vertragsjahr=vertragsjahr)
        self._besoldungsgruppe = besoldungsgruppe

    def __str__(self):
        return (f"{Person.__str__(self)}, {Angestellter.__str__(self)} "
                f"und gleichzeitig Dozent mit Besoldungsgruppe {self._besoldungsgruppe}")


# ============= Тестирование =============
s2 = Studierender(name="Petra", geburtsjahr=1999, matrNr=123457)
d1 = Dozent(name="Hans", geburtsjahr=1984, besoldungsgruppe="W2")
p1 = Person(name="Julia", geburtsjahr=2001)

personen_liste = [s2, p1, d1]

for p in personen_liste:
    print(type(p).__name__)
    p.drucken()
    print("-" * 70)