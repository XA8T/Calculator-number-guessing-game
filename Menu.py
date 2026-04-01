from random import (randint)
import random

def verlassen():
    exit()

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
            if zahl_2 == 0:
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

def blackjack():
    player_value = 0
    dealer_value = 0
    dealer_value_hidden = 0
    cards = [i for i in range(1, 11)] * 4
    random.shuffle(cards)
    dealer_value += cards.pop()
    dealer_value_hidden += cards.pop()
    print("Dealer hat", dealer_value, "+ Unbekannte ")
    player_value += cards.pop()
    player_value += cards.pop()
    print("Du hast", player_value)
    while True:
        aktion = str(input("( Hit / Stand ) "))
        if aktion == "Hit":
            player_value += cards.pop()
            print("Du hast", player_value)
            if player_value > 21:
                print("Bust! ")
                return
            else:
                pass

        elif aktion == "Stand":
            break
    while True:
        if dealer_value + dealer_value_hidden <= 16:
            dealer_value += cards.pop()
            if dealer_value + dealer_value_hidden > 21:
                print("Dealer hat Verloren! Da er 21 überschritten hat")
                print("Dealer hat", dealer_value + dealer_value_hidden)
                return
            else:
                pass
        else:
            break

    if player_value > dealer_value + dealer_value_hidden:
        print("Dealer hat nur",dealer_value + dealer_value_hidden, "Du hingegen hast", player_value)
        print("Du hast Gewonnen! ")

    elif player_value < dealer_value + dealer_value_hidden:
        print("Du hast nur", player_value, "Der Dealer hingegen hat", dealer_value + dealer_value_hidden)
        print("Du hast Verloren! ")

    elif player_value == dealer_value + dealer_value_hidden:
        print("Ihr beide habt", player_value)
        print("Gleichstand! ")
        print(dealer_value + dealer_value_hidden)

while True:
    menu = str(input("Welches Programm soll gestartet werden ( Verlassen / Taschenrechner / Zahlenspiel / Blackjack ) "))
    if menu == "Taschenrechner":
        taschenrechner()
        pass

    elif menu == "Zahlenspiel":
        ratespiel()
        pass

    elif menu == "Blackjack":
        blackjack()

    elif menu == "Verlassen":
        verlassen()
