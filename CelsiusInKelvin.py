from tkinter import *

fenster = Tk()
fenster.title("Temperatur Umwandler")

def action():
    temp_str = eingabefeld.get()
    try:
        temp = float(temp_str)
    except ValueError:
        message = "Keine Zahl"
        ergebnis_label.configure(text=message)
    wahl = variable.get()
    if wahl == u1:
        message = temp_str + "° = " + str(C_K(temp)) + "K"
    elif wahl == u2:
        message = temp_str + "° = " + str(C_F(temp)) + "F"
    elif wahl == u3:
        message = temp_str + "K = " + str(K_C(temp)) + "°"
    elif wahl == u4:
        message = temp_str + "K = " + str(K_F(temp)) + "F"
    elif wahl == u5:
        message = temp_str + "F = " + str(F_C(temp)) + "°"
    elif wahl == u6:
        message = temp_str + "F = " + str(F_K(temp)) + "K"
    ergebnis_label.configure(text=message)

def C_K(t):
    t = t + 273.15
    return t
def C_F(t):
    t = (t*(9/5)) + 32
    return t
def K_C(t):
    t = t - 273.15
    return t
def K_F(t):
    t = (9/5)*(t - 273.15) + 32
    return t
def F_C(t):
    t = (5/9)*(t - 32)
    return t
def F_K(t):
    t = (t - 32)*(5/9) + 273.15
    return t




anweisungs_label = Label(fenster, text="*******TEMPERATUR UMWANDLER*******\n\
1) Gewünschte Umrechnung wählen\n\
2) Temperatur eingeben         \n\
3) Taste ~Umrechnen~ drücken      ")

u1 = "von Celsius nach Klevin"
u2 = "von Celsius nach Fahrenheit"
u3 = "von Kelvin nach Celsius"
u4 = "von Kelvin nach Fahrenheit"
u5 = "von Fahrenheit nach Celsius"
u6 = "von Fahrenheit nach Kelvin"

variable = StringVar(fenster)
variable.set("von Celsius nach Klevin")
auswahl_button = OptionMenu(fenster, variable, u1, u2, u3, u4, u5, u6)

umrechnen_button = Button(fenster, text="Umrechnen", command = action)
eingabefeld = Entry(fenster, bd=5, width=40)
ausgabe_label = Label(fenster, text="Ausgabe:")
ergebnis_label = Label(fenster, text="")

fenster.geometry("400x350")
anweisungs_label.place(x = 100, y = 0, width=200, height=110)
auswahl_button.place(x = 50, y = 120, width=300, height=50)
umrechnen_button.place(x = 230, y = 210, width=130, height=30)
eingabefeld.place(x = 40, y = 210, width=130, height=30)
ausgabe_label.place(x = 40, y = 280)
ergebnis_label.place(x = 100, y = 280)

fenster.mainloop()