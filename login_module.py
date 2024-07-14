import tkinter as tk
from PIL import Image, ImageTk
import os
import desktop_module

# Archivo para almacenar los usuarios y contraseñas
ARCHIVO_USUARIOS = "usuarios.txt"

# Diccionario para almacenar los nombres de usuario y las contraseñas
usuarios = {}

# Elementos de la interfaz de inicio de sesión
username_entry = None
password_entry = None
error_label = None
root = None

def cargar_usuarios():
    """
    Cargar usuarios desde el archivo al iniciar el programa.
    """
    try:
        with open(ARCHIVO_USUARIOS, "r") as f:
            for linea in f:
                username, password = linea.strip().split(":")
                usuarios[username] = password
    except FileNotFoundError:
        # Si el archivo no existe, no hay usuarios registrados aún
        pass

def guardar_usuarios():
    """
    Guardar usuarios en el archivo.
    """
    with open(ARCHIVO_USUARIOS, "w") as f:
        for username, password in usuarios.items():
            f.write(f"{username}:{password}\n")

def login():
    """
    Función para iniciar sesión.
    """
    username = username_entry.get()
    password = password_entry.get()
    
    # Verificar si el nombre de usuario existe y la contraseña es correcta
    if username in usuarios and usuarios[username] == password:
        # Si el usuario y la contraseña son válidos, puedes abrir la interfaz principal
        user_dir = os.path.join("usuarios", username)
        root.withdraw()  # Ocultar la ventana principal en lugar de destruirla
        desktop_module.open_main_interface(root, username, user_dir)
    else:
        # Si no son válidos, muestra un mensaje de error
        error_label.config(text="Usuario o contraseña incorrectos")

def registrar_usuario():
    """
    Función para registrar un nuevo usuario.
    """
    global username_entry, password_entry, error_label, root

    username = username_entry.get()
    password = password_entry.get()
    
    # Verificar si el nombre de usuario ya existe
    if username in usuarios:
        error_label.config(text="El nombre de usuario ya está registrado")
    else:
        # Registrar el nuevo usuario
        usuarios[username] = password
        guardar_usuarios()
        error_label.config(text="Usuario registrado correctamente")

        # Crear el directorio del nuevo usuario
        try:
            dir_usuario = os.path.join("usuarios", username)
            os.mkdir(dir_usuario)
            print(f"Directorio del usuario '{username}' creado correctamente.")
        except OSError as e:
            print(f"No se pudo crear el directorio del usuario '{username}': {e}")

def ventana_login():
    global username_entry, password_entry, error_label, root

    # Crear la ventana principal
    root = tk.Tk()
    root.title("JM Sistem - Inicio de sesión")

    # Maximizar la ventana del escritorio para que ocupe toda la pantalla
    root.attributes("-fullscreen", True)

    # Cargar usuarios al iniciar el programa
    cargar_usuarios()

    # Obtener la ruta absoluta del directorio actual
    dir_actual = os.path.dirname(os.path.abspath(__file__))

    # Cargar y mostrar la imagen del usuario
    image_path = os.path.join(dir_actual, "imagenes", "logo.png")
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    user_image_label = tk.Label(root, image=photo)
    user_image_label.pack(pady=30)

    # Crear los elementos de la interfaz de inicio de sesión
    username_label = tk.Label(root, text="Usuario:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Contraseña:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")  # Para ocultar la contraseña
    password_entry.pack()

    login_button = tk.Button(root, text="Iniciar sesión", command=login)
    login_button.pack(pady=8)

    register_button = tk.Button(root, text="Registrar usuario", command=registrar_usuario)
    register_button.pack(pady=8)

    error_label = tk.Label(root, fg="red")
    error_label.pack()

    # Agregar botón de salir en la esquina superior derecha
    exit_button = tk.Button(root, text="Salir", command=root.destroy)
    exit_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)
    
    # Ejecutar el bucle de eventos de la ventana
    root.mainloop()

if __name__ == "__main__":
    ventana_login()