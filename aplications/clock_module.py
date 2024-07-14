import tkinter as tk
from math import cos, sin, pi
import time

def update_clock():
    # Obtener el tiempo actual
    current_time = time.localtime()
    hour = current_time.tm_hour % 12  # Convertir a formato de 12 horas
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    # Calcular los ángulos de las manecillas
    hour_angle = (hour * 30) + (minute * 0.5)  # Cada hora representa 30 grados, cada minuto 0.5 grados
    minute_angle = (minute * 6) + (second * 0.1)  # Cada minuto representa 6 grados, cada segundo 0.1 grados
    second_angle = second * 6  # Cada segundo representa 6 grados
    
    # Borrar el contenido anterior del canvas
    canvas.delete("all")
    
    # Dibujar los números del reloj
    for i in range(1, 13):
        angle = (i - 3) * 30  # Desplazar los números para que comiencen desde el 12 en punto
        x = 150 + 90 * cos(angle * (pi / 180))
        y = 150 + 90 * sin(angle * (pi / 180))
        canvas.create_text(x, y, text=str(i), font=("Arial", 12), fill="white")
    
    # Dibujar las manecillas del reloj
    draw_hand(50, hour_angle, 30, "white")  # Manecilla de las horas
    draw_hand(80, minute_angle, 20, "white")  # Manecilla de los minutos
    draw_hand(100, second_angle, 5, "white")  # Manecilla de los segundos
    
    # Llamar a esta función nuevamente después de 1000 milisegundos (1 segundo)
    root.after(1000, update_clock)

def draw_hand(length, angle, width, color):
    x1 = 150 + length * sin(angle * (pi / 180))
    y1 = 150 - length * cos(angle * (pi / 180))
    x2 = 150 + 10 * sin((angle + 180) * (pi / 180))  # Punto opuesto al extremo de la manecilla
    y2 = 150 - 10 * cos((angle + 180) * (pi / 180))
    x3 = 150 + 10 * sin((angle + 90) * (pi / 180))  # Punto de la punta del triángulo
    y3 = 150 - 10 * cos((angle + 90) * (pi / 180))
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)

def start_clock():
    
    global canvas,root
    
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Reloj Analógico")

    # Crear un canvas para dibujar el reloj
    canvas = tk.Canvas(root, width=300, height=300, bg="black")
    canvas.pack()

    # Llamar a la función update_clock para iniciar el reloj
    update_clock()

    # Ejecutar el bucle de eventos de la ventana
    root.mainloop()
