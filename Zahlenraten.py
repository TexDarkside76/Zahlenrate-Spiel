import random

x = random.randint(0,100)


def eingabe():
    while True:
        try:
            y = int(input("Bitte geben Sie eine Zahl zwischen 0 und 100 ein:\n"))
            return y
        except ValueError:
           print("ERROR")




def ausgabe(eingabe,counter):
    if eingabe==x:
        print()
        print(f"Glückwunsch Sie haben {counter} Versuche gebraucht")
    elif eingabe<x:
        print()
        print("Ihre Zahl ist zu klein, versuchen sie es erneut")
        
    else:
        print()
        print("Ihre Zahl ist zu groß, versuchen sie es erneut")


counter = 0
while True:
    userinput = eingabe()
    counter += 1
    ausgabe(userinput,counter)

    if userinput == x:
        break


            