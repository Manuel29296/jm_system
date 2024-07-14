import tkinter as tk
from tkinter import filedialog, messagebox
import os

def open_folder():
    folder_path = filedialog.askdirectory(initialdir=user_dir)
    if folder_path:
        # Convertir ambas rutas a absolutas para la comparación
        abs_folder_path = os.path.abspath(folder_path)
        abs_user_dir = os.path.abspath(user_dir)
        
        # Verificar si la carpeta seleccionada está dentro del directorio del usuario
        if os.path.commonpath([abs_folder_path, abs_user_dir]) == abs_user_dir:
            show_files_in_folder(folder_path)
        else:
            messagebox.showwarning("Advertencia", "No se puede acceder a carpetas fuera de tu directorio de usuario.")

def show_files_in_folder(folder_path):
    # Convertir ambas rutas a absolutas para la comparación
    abs_folder_path = os.path.abspath(folder_path)
    abs_user_dir = os.path.abspath(user_dir)
    
    # Verificar si la carpeta es subdirectorio del directorio del usuario
    if os.path.commonpath([abs_folder_path, abs_user_dir]) != abs_user_dir:
        messagebox.showwarning("Advertencia", "No se puede acceder a carpetas fuera de tu directorio de usuario.")
        return
    
    current_folder.set(folder_path)
    files_list.delete(0, tk.END)
    for file in os.listdir(folder_path):
        files_list.insert(tk.END, file)

def create_folder():
    folder_name = folder_name_entry.get()
    if folder_name:
        try:
            os.mkdir(os.path.join(current_folder.get(), folder_name))
            show_files_in_folder(current_folder.get())
        except OSError:
            messagebox.showerror("Error", "No se pudo crear la carpeta.")
    else:
        messagebox.showwarning("Advertencia", "Ingrese un nombre para la carpeta.")

def delete_item():
    selection = files_list.curselection()
    if selection:
        item = files_list.get(selection)
        item_path = os.path.join(current_folder.get(), item)
        try:
            if os.path.isdir(item_path):
                os.rmdir(item_path)
            else:
                os.remove(item_path)
            show_files_in_folder(current_folder.get())
        except OSError:
            messagebox.showerror("Error", "No se pudo eliminar el archivo o carpeta.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un archivo o carpeta para eliminar.")

def create_file():
    file_name = file_name_entry.get()
    if file_name:
        file_path = os.path.join(current_folder.get(), file_name)
        try:
            with open(file_path, 'w'):
                pass
            show_files_in_folder(current_folder.get())
        except OSError:
            messagebox.showerror("Error", "No se pudo crear el archivo.")
    else:
        messagebox.showwarning("Advertencia", "Ingrese un nombre para el archivo.")

def file_manager(user_directory):
    global current_folder, file_name_entry, files_list, folder_name_entry, user_dir
    user_dir = os.path.abspath(user_directory)  # Almacenar el directorio del usuario para su uso en open_folder
    fm_window = tk.Toplevel()
    fm_window.title("Gestor de Archivos - " + user_dir)

    current_folder = tk.StringVar()
    current_folder.set(user_dir)

    folder_name_label = tk.Label(fm_window, text="Nombre de la carpeta:")
    folder_name_label.grid(row=0, column=0, sticky="w")
    folder_name_entry = tk.Entry(fm_window)
    folder_name_entry.grid(row=0, column=1)
    create_folder_button = tk.Button(fm_window, text="Crear Carpeta", command=create_folder)
    create_folder_button.grid(row=0, column=2)

    file_name_label = tk.Label(fm_window, text="Nombre del archivo:")
    file_name_label.grid(row=1, column=0, sticky="w")
    file_name_entry = tk.Entry(fm_window)
    file_name_entry.grid(row=1, column=1)
    create_file_button = tk.Button(fm_window, text="Crear Archivo", command=create_file)
    create_file_button.grid(row=1, column=2)

    delete_button = tk.Button(fm_window, text="Eliminar", command=delete_item)
    delete_button.grid(row=2, column=0, columnspan=3)

    files_list = tk.Listbox(fm_window, width=50)
    files_list.grid(row=3, column=0, columnspan=3)

    open_folder_button = tk.Button(fm_window, text="Abrir Carpeta", command=open_folder)
    open_folder_button.grid(row=4, column=0, columnspan=3)

    # Mostrar los archivos de la carpeta del usuario al iniciar
    show_files_in_folder(user_dir)

    fm_window.mainloop()