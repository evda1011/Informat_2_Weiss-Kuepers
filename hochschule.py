import datetime
im

class Person:
    """ Klasse zur Repräsentation von Personen """
    def __init__(self, name=None, geburtsjahr=None):
        self._name = name
        self._geburtsjahr = geburtsjahr

    def __str__(self):
        return f"Person: {self.name}, Geburtsjahr: {self.geburtsjahr}"


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

