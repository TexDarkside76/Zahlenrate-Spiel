import tkinter as tk
import random

x = random.randint(1,100)
print("Gesuchte zahlt", x)
counter=0

def ausgabe(eingabe):
    global counter
    counter+=1
    if eingabe==x:
        ausgabe_text.set(f"Richtig! Zahl: {eingabe}\n Versuche: {counter}")
    elif eingabe<x:
        print()
        print(eingabe)
        ausgabe_text.set(f"{eingabe} ist zu klein, versuchen sie es erneut")
        
    else:
        print()
        print(eingabe)
        ausgabe_text.set(f"{eingabe} ist zu groß, versuchen sie es erneut")













###########################################
##################GUI######################
###########################################



root = tk.Tk()
root.geometry("1024x1536")

canvas = tk.Canvas(root, width=1024, height=1536)
canvas.pack()


#Hintergrundbild
bild = tk.PhotoImage(file="Hintergrund.png")
canvas.create_image(0, 0, anchor="nw", image=bild)


#Ausgabe von Text
ausgabe_text = tk.StringVar()
ausgabe_label = tk.Label(root, textvariable=ausgabe_text, font=("Times",18))
canvas.create_window(512,150, window=ausgabe_label)


canvas.create_text(
    512,
    60,
    text="Ich habe mir eine Zahl zwischen 1 und 100 gedacht",
    font=("Times", 24, "bold", "italic")
)

start_x = 250
start_y = 425
abstand = 60

#Button erstellen mit for schleife
for row in range(10):
    for col in range(10):

        num = row * 10 + col + 1

        def make_command(n):
            return lambda: ausgabe(n)

        button = tk.Button(
            root,
            text=str(num),
            width=4,
            command=make_command(num)
        )

        x_pos = start_x + col * abstand
        y_pos = start_y + row * abstand

        canvas.create_window(x_pos, y_pos, window=button)

root.mainloop()





