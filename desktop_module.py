import tkinter as tk
from PIL import Image, ImageTk
import time
import os
from aplications import clock_module
from aplications import calculate_module
from aplications import file_manager_module
from aplications import edit_file_module
from aplications import open_media_module
from aplications import music_module
from aplications import google_module
from aplications import game_snake_module

def open_main_interface(root, username, user_dir):
    desktop_window = tk.Toplevel(root)
    desktop_window.title("Escritorio - " + username)
    desktop_window.attributes("-fullscreen", True)
    desktop_window.update_idletasks()
    window_width = desktop_window.winfo_width()
    window_height = desktop_window.winfo_height()

    taskbar = tk.Frame(desktop_window, bg="gray", height=30)
    taskbar.pack(side=tk.BOTTOM, fill=tk.X)
    start_menu_button = tk.Button(taskbar, text="Inicio", command=lambda: open_start_menu(desktop_window))
    start_menu_button.pack(side=tk.LEFT)
    exit_button = tk.Button(taskbar, text="Salir", command=desktop_window.destroy)
    exit_button.pack(side=tk.RIGHT, padx=10)
    notification_label = tk.Label(taskbar, text="Notificación importante", bg="yellow")
    notification_label.pack(side=tk.RIGHT)
    current_time = time.strftime("%H:%M:%S")
    time_label = tk.Label(desktop_window, text="Hora actual: " + current_time)
    time_label.pack()

    background_image = Image.open("imagenes/escritorio.png")
    resized_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(resized_image)
    background_label = tk.Label(desktop_window, image=background_photo)
    background_label.image = background_photo
    background_label.pack(fill=tk.BOTH, expand=True)

    icon_size = (64, 64)
    app1_icon = Image.open("imagenes/carpeta.png").resize(icon_size)
    app1_photo = ImageTk.PhotoImage(app1_icon)
    app1_button = tk.Button(desktop_window, image=app1_photo, command=lambda: file_manager_module.file_manager(user_dir))
    app1_button.image = app1_photo
    app1_button.place(x=50, y=50)

    app2_icon = Image.open("imagenes/archivo.png").resize(icon_size)
    app2_photo = ImageTk.PhotoImage(app2_icon)
    app2_button = tk.Button(desktop_window, image=app2_photo, command=lambda: edit_file_module.edit_file(os.path.join("usuarios", username), desktop_window))
    app2_button.image = app2_photo
    app2_button.place(x=150, y=50)

    app3_icon = Image.open("imagenes/reloj.png").resize(icon_size)
    app3_photo = ImageTk.PhotoImage(app3_icon)
    app3_button = tk.Button(desktop_window, image=app3_photo, command=lambda: clock_module.start_clock())
    app3_button.image = app3_photo
    app3_button.place(x=250, y=50)

    app4_icon = Image.open("imagenes/calculadora.png").resize(icon_size)
    app4_photo = ImageTk.PhotoImage(app4_icon)
    app4_button = tk.Button(desktop_window, image=app4_photo, command=lambda: calculate_module.start_calculate())
    app4_button.image = app4_photo
    app4_button.place(x=350, y=50)

    app5_icon = Image.open("imagenes/camara.png").resize(icon_size)
    app5_photo = ImageTk.PhotoImage(app5_icon)
    app5_button = tk.Button(desktop_window, image=app5_photo, command=lambda: open_media_module.open_media_viewer())
    app5_button.image = app5_photo
    app5_button.place(x=450, y=50)
    
    app6_icon = Image.open("imagenes/musica.png").resize(icon_size)
    app6_photo = ImageTk.PhotoImage(app6_icon)
    app6_button = tk.Button(desktop_window, image=app6_photo, command=lambda: music_module.start_music_player())
    app6_button.image = app6_photo
    app6_button.place(x=550, y=50)
    
    app7_icon = Image.open("imagenes/google.png").resize(icon_size)
    app7_photo = ImageTk.PhotoImage(app7_icon)
    app7_button = tk.Button(desktop_window, image=app7_photo, command=lambda: google_module.open_browser_from_application())
    app7_button.image = app7_photo
    app7_button.place(x=650, y=50)
    
    app8_icon = Image.open("imagenes/serpiente.png").resize(icon_size)
    app8_photo = ImageTk.PhotoImage(app8_icon)
    app8_button = tk.Button(desktop_window, image=app8_photo, command=lambda: game_snake_module.main())
    app8_button.image = app8_photo
    app8_button.place(x=750, y=50)

def open_start_menu(desktop_window):
    pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema Operativo")
    user_dir = "ruta_al_directorio_del_usuario"
    open_main_interface(root, "Usuario Ejemplo", user_dir)
    root.mainloop()