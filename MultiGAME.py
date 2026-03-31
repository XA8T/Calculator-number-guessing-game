from random import randint

def taschenrechner():
    while True:
        zahl_1 = float(input("Wie lautet deine erste Zahl? "))
        op = str(input("Wie lautet dein Operator? "))
        zahl_2 = float(input("Wie lautet deine zweite Zahl? "))

        if op == "+":
            print(zahl_1 + zahl_2)
        elif op == "-":
            print(zahl_1 - zahl_2)
        elif op == "*":
            print(zahl_1 * zahl_2)
        elif op == "/":
            if zahl_1 == 0:
                print("Division durch 0 nicht möglich")
            elif zahl_2 == 0:
                print("Division durch 0 nicht möglich")
            else:
                print(zahl_1 / zahl_2)
        elif op == "**":
            print(zahl_1 ** zahl_2)
        else:
            print("ungültiger Operator! ")
        eingabe = str(input("Möchtest du nochmal Rechnen? (y / n) "))
        if eingabe == "y":
            pass
        elif eingabe == "n":
            break
        else:
            pass

def ratespiel():
    zahl = randint(1, 100)
    while True:
        raten = int(input("Errate die Zahl zwischen 1-100 "))
        if zahl == raten:
            print("Du hast erfolgreich die Zahl", zahl, "erfolgreich erraten!")
            eingabe = str(input("Willst du das Spiel nochmal spielen? (y / n) "))
            if eingabe == "y":
                zahl = randint(1, 100)
                pass
            elif eingabe == "n":
                break
            else:
                print("Versuche es erneut")


        elif zahl > raten:
            print("Die Zahl ist größer als", raten, "versuche es erneut ")

        else:
            print("Die Zahl ist kleiner als", raten, "versuche es erneut ")

tools = {
    "1": taschenrechner,
    "2": ratespiel,
}

while True:
    menu = str(input("Welches Programm soll gestartet werden ( Verlassen / Taschenrechner / Zahlenspiel ) "))
    if menu == "Taschenrechner":
        taschenrechner()
        pass

    elif menu == "Zahlenspiel":
        ratespiel()
        pass

    elif menu == "Verlassen":
        exit()