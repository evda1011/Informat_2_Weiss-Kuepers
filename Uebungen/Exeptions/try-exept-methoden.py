# try-exept
"""try:
    # нормальный код
    x = 10 / 0
except ZeroDivisionError as e:      # можно ловить конкретные ошибки
    print("Fehler: Division durch Null!", e)
except Exception as e:              # общее исключение
    print("Unbekannter Fehler:", e)
else:
    # выполняется, если ошибок НЕ было
    print("Alles gut gelaufen")
finally:
    # выполняется ВСЕГДА (для очистки ресурсов)
    print("Aufräumen...")"""



# =============================================
# try - except Beispiel
# =============================================
"""
try:
    a = int(input("Dividend: "))
    b = int(input("Divisor:  "))

    print(f"Quotient = {a / b}")
    print(f"Summe    = {a + b}")

except ValueError:
    print("Fehler: Es wurden keine gültigen Zahlen eingegeben!")

except ZeroDivisionError:
    print("Fehler: Division durch 0 ist nicht erlaubt!")

except Exception as e:
    print(f"Unerwarteter Fehler: {type(e).__name__} - {e}")

else:
    print("✅ Alles erfolgreich ausgeführt!")

finally:
    print("--- finally-Block: Wird immer ausgeführt ---")
"""




try:
    a = int(input("Dividend:")) # könnte auch vor dem "try" stehen!
    b = int(input("Divisor:")) # könnte auch vor dem "try" stehen!
    print(f"Quotient = {a/b}") # muss in den try-except-block!
    print(f"Summe = {a+b}") # muss in den try-except-block!
except ValueError:
    print("Zahlenkonvertierung fehlgeschlagen")
except ZeroDivisionError:
    print("Division durch 0 unzulässig")
except:
    print("Etwas anderes ist nicht in Ordnung.")
