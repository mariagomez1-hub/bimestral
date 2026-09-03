from tkinter import *
import random

# ------------------
# variables globales
# ------------------
BASE = 460
ALTURA = 220
x_pollito = 100
y_pollito = 100

# -------------------
# funciones
# -------------------

# Funcion para mover el pollito a la derecha
def mover_derecha(event=None):
    # Borrar canvas
    c.delete("all")
    # Mover pollito
    global x_pollito
    global pollito
    if x_pollito < BASE:
        x_pollito = x_pollito + 10
    else:
        x_pollito = 0
    pollito = c.create_image(x_pollito,y_pollito,image=img_pollito)


# Funcion para mover el pollito
def mover_izquierda(event=None):
    # Borrar canvas
    c.delete("all")
    # Mover pollito
    global x_pollito
    global pollito
    if x_pollito > 0:
        x_pollito = x_pollito - 10
    else:
        x_pollito = BASE
    pollito = c.create_image(x_pollito,y_pollito,image=img_pollito)


# Funcion para mover el pollito
def mover_arriba(event=None):
    # Borrar canvas
    c.delete("all")
    # Mover pollito
    global y_pollito
    global pollito
    if y_pollito > 0:
        y_pollito = y_pollito - 10
    else:
        y_pollito = ALTURA
    pollito = c.create_image(x_pollito,y_pollito,image=img_pollito)

# Funcion para mover el pollito
def mover_abajo(event=None):
    # Borrar canvas
    c.delete("all")
    # Mover pollito
    global y_pollito
    global pollito
    if y_pollito < ALTURA:
        y_pollito= y_pollito + 10
    else:
        y_pollito = 0
    pollito = c.create_image(x_pollito,y_pollito,image=img_pollito)


# -----------------
# ventana principal
# -----------------
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="gray")


# frame de graficacion
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="pink", width=480, height=240)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

# ubicacion inicial del pollito
img_pollito = PhotoImage(file="img/pollito.png")
pollito = c.create_image(x_pollito,y_pollito,image=img_pollito)

#------------------------
# Movimientos con teclado
#------------------------
ventana_principal.bind("<KeyPress-Up>",mover_arriba)
ventana_principal.bind("<KeyPress-Down>",mover_abajo)
ventana_principal.bind("<KeyPress-Left>",mover_izquierda)
ventana_principal.bind("<KeyPress-Right>",mover_derecha)

# frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10,y=260)

# botones movimiento
img_up = PhotoImage(file="img/up.png")
bt_up = Button(frame_controles, image=img_up, command=mover_arriba)
bt_up.place(x=208,y=19)

img_down = PhotoImage(file="img/down.png")
bt_down = Button(frame_controles, image=img_down, command=mover_abajo)
bt_down.place(x=208,y=147)

# boton para mover hacia la derecha
img_right = PhotoImage(file="img/right.png")
bt_right = Button(frame_controles, image=img_right, command=mover_derecha)
bt_right.place(x=272,y=83)

img_left = PhotoImage(file="img/left.png")
bt_left = Button(frame_controles, image=img_left, command=mover_izquierda)
bt_left.place(x=144,y=83)


# desplegar ventana
ventana_principal.mainloop()