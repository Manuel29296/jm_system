import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os
import threading

# Inicializar Pygame mixer
pygame.mixer.init()

current_file = None  # Definir current_file como una variable global

def play_music():
    global current_file
    if current_file:
        try:
            pygame.mixer.music.load(current_file)
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo reproducir el archivo: {e}")
    else:
        messagebox.showinfo("Información", "No hay archivo seleccionado")

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def open_file():
    global current_file
    current_file = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3;*.wav")])
    if current_file:
        file_label.config(text=os.path.basename(current_file))  # Acceder a file_label como variable global

def play_music_thread():
    # Ejecutar la reproducción de música en un hilo separado
    music_thread = threading.Thread(target=play_music)
    music_thread.start()

def start_music_player():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Reproductor de Música")

    global file_label  # Definir file_label como variable global

    # Botón para abrir archivo
    open_button = tk.Button(root, text="Abrir Archivo", command=open_file)
    open_button.pack(pady=10)

    # Etiqueta para mostrar el archivo seleccionado
    file_label = tk.Label(root, text="No hay archivo seleccionado")
    file_label.pack(pady=5)

    # Botón para reproducir
    play_button = tk.Button(root, text="Reproducir", command=play_music_thread)
    play_button.pack(pady=5)

    # Botón para pausar
    pause_button = tk.Button(root, text="Pausar", command=pause_music)
    pause_button.pack(pady=5)

    # Botón para reanudar
    resume_button = tk.Button(root, text="Reanudar", command=resume_music)
    resume_button.pack(pady=5)

    # Botón para detener
    stop_button = tk.Button(root, text="Detener", command=stop_music)
    stop_button.pack(pady=5)

    # Ejecutar la aplicación
    root.mainloop()