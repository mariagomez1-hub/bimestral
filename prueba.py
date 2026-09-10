from tkinter import *
import random

# ------------------
# variables globales
# ------------------
BASE = 460
ALTURA = 400

x_pollito = 230
y_pollito = 360

carros = []


# ------------------
# funciones
# ------------------

# dibujar el escenario
def dibujar_escenario():
    c.delete("escenario")

    # fondo de arriba y abajo
    c.create_rectangle(0, 0, BASE, 80, fill="pink", tags="escenario")
    c.create_rectangle(0, 320, BASE, ALTURA, fill="pink", tags="escenario")

    # escenario
    c.create_rectangle(0, 80, BASE, 320, fill="gray", tags="escenario")

    # lineas de la carretera
    for y in range(120, 320, 50):
        c.create_rectangle(0, y, BASE, y + 5,
        fill="white", tags="escenario")


# crear los carros
def crear_carros():
    global carros
    carros = []
    colores = [ "blue", "purple"]
    posiciones = [ (50, 100, 130, 140, 5),(300, 150, 390, 190, -5),(120, 210, 210, 250, 5),(330, 260, 420, 300, -5)]
    for x1, y1, x2, y2, velocidad in posiciones:
        color = random.choice(colores)
        carro = c.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", tags="carro")
        carros.append([carro, velocidad])


# dibujar el pollito
def dibujar_pollito():
    c.delete("pollito")

    # cuerpo
    c.create_oval(x_pollito - 15, y_pollito - 15, x_pollito + 15, y_pollito + 15, fill="yellow", outline="black", tags="pollito")


# mover carros
def mover_carros():
    for carro in carros:
        objeto = carro[0]
        velocidad = carro[1]
        c.move(objeto, velocidad, 0)
        coordenadas = c.coords(objeto)
        if velocidad > 0 and coordenadas[2] > BASE:
            c.move(objeto, -BASE - 100, 0)
        elif velocidad < 0 and coordenadas[0] < 0:
            c.move(objeto, BASE + 100, 0)


# comprobar choque
def comprobar_colision():
    pollito_coords = ( x_pollito - 15, y_pollito - 28, x_pollito + 22, y_pollito + 24)

    for carro in carros:

        coords = c.coords(carro[0])

        if (pollito_coords[2] > coords[0] and
            pollito_coords[0] < coords[2] and
            pollito_coords[3] > coords[1] and
            pollito_coords[1] < coords[3]):

            perder()


# ganar
def ganar():
    c.create_text(BASE / 2, ALTURA / 2,text="¡GANASTE!", font=("Arial", 30, "bold"),fill="white",tags="mensaje")


# perder
def perder():
    c.create_text(BASE / 2,ALTURA / 2,text="¡Perdiste!",font=("Arial", 22, "bold"),fill="red",tags="mensaje")


# movimiento del pollito
def mover_arriba(event=None):
    global y_pollito

    if y_pollito > 20:
        y_pollito -= 10
        dibujar_pollito()
    comprobar_colision()

    if y_pollito <= 80:
        ganar()


def mover_abajo(event=None):
    global y_pollito
    if y_pollito < ALTURA - 20:
        y_pollito += 10
    dibujar_pollito()
    comprobar_colision()


def mover_izquierda(event=None):
    global x_pollito
    if x_pollito > 20:
        x_pollito -= 10
    dibujar_pollito()
    comprobar_colision()


def mover_derecha(event=None):
    global x_pollito
    if x_pollito < BASE - 20:
        x_pollito += 10
    dibujar_pollito()
    comprobar_colision()


# animación de los carros
def actualizar():
    mover_carros()
    comprobar_colision()
    ventana_principal.after(50, actualizar)


# ------------------
# ventana principal
# ------------------

ventana_principal = Tk()
ventana_principal.title("pollito Cruza la Avenida")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")


# canvas
c = Canvas( ventana_principal, width=BASE,height=ALTURA,bg="green")

c.place(x=20, y=20)


# crear escenario
dibujar_escenario()

# crear carros
crear_carros()

# dibujar pollito
dibujar_pollito()


# ------------------
# controles teclado
# ------------------

ventana_principal.bind("<Up>", mover_arriba)
ventana_principal.bind("<Down>", mover_abajo)
ventana_principal.bind("<Left>", mover_izquierda)
ventana_principal.bind("<Right>", mover_derecha)


# iniciar movimiento
actualizar()


# desplegar ventana
ventana_principal.mainloop()