# ── Datentypen ──────────────────────────────────────────
results = []  # list  – Verlauf speichern

# ── Funktionen ──────────────────────────────────────────
# TODO: Funktionen für die vier Grundrechenarten implementieren
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Fehler: Division durch null!")
        return None
    return a / b

def wurzel(a):
    if a < 0:
        print("Fehler: Negative Zahl für Wurzel!")
        return None
    return a ** 0.5

def potenz(a, b):
    return a ** b


def show_history():
    if not results:
        print("Keine Berechnungen im Verlauf.")
    else:
        print("Verlauf:")
        for entry in results:
            print(entry)

# ── Hauptprogramm ───────────────────────────────────────
def start_calculator():
    print("=== Taschenrechner ===")

    while True:                        # Kontrollstruktur
        print("\n1: Addieren")
        print("2: Subtrahieren")
        print("3: Multiplizieren")
        print("4: Dividieren")
        print("5: Potenzieren")
        print("6: Wurzeln")
        print("7: Verlauf anzeigen")
        print("8: Beenden")

        choice = input("Wähle: ").strip()      # str

        if choice == "8":              #8 Kontrollstruktur
            print("Tschüss!")
            break

        if choice == "6":
            show_history()
            continue

        # Zahlen einlesen
        a = float(input("Erste Zahl: "))   # float
        b = float(input("Zweite Zahl: "))  # float

        # Berechnung je nach Auswahl
        if choice == "1":
            result = add(a, b)
            op = "+"
        elif choice == "2":
            result = subtract(a, b)
            op = "-"
        elif choice == "3":
            result = multiply(a, b)
            op = "*"
        elif choice == "4":
            result = divide(a, b)
            op = "/"
        elif choice == "5":
            result = a ** b
            op = "**"
        elif choice == "6":
            result = a ** 0.5
            op = "**0.5"
        elif choice == "7":
            show_history()
            continue
        elif choice == "8":
            print("Tschüss!")
            break
        else:
            print("Ungültige Eingabe!")
            continue

        print(f"Ergebnis: {result}")
        results.append(f"{a} {op} {b} = {result}")  # list befüllen

# Programm starten
start_calculator()
