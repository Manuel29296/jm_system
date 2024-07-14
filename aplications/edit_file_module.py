import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os

def ensure_directory_exists(directory):
    """
    Verifica que el directorio exista, si no, lo crea.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def edit_file(user_dir, root_window):
    """
    Función para abrir el editor de archivos.
    """
    ensure_directory_exists(user_dir)
    file_path = ask_open_filename_in_directory(user_dir)
    
    if file_path:
        try:
            abs_file_path = os.path.abspath(file_path)
            abs_user_dir = os.path.abspath(user_dir)
            
            # Verificar si el archivo seleccionado está dentro del directorio del usuario
            if os.path.commonpath([abs_file_path, abs_user_dir]) == abs_user_dir:
                with open(abs_file_path, 'r+') as file:
                    file_content = file.read()
                
                edit_window = tk.Toplevel(root_window)
                edit_window.title(f"Editar {os.path.basename(abs_file_path)}")
                
                text_area = scrolledtext.ScrolledText(edit_window, width=40, height=10)
                text_area.pack(fill=tk.BOTH, expand=True)
                text_area.insert(tk.END, file_content)
                
                save_button = tk.Button(edit_window, text="Guardar", command=lambda: save_file(abs_file_path, text_area.get("1.0", tk.END)))
                save_button.pack()
                
                edit_window.transient(root_window)
                edit_window.grab_set()
                edit_window.lift()
                
                edit_window.mainloop()
            else:
                messagebox.showwarning("Advertencia", "No se puede acceder a archivos fuera de tu directorio de usuario.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo para editar: {e}")

def ask_open_filename_in_directory(directory):
    """
    Función para abrir un diálogo de selección de archivos restringido a un directorio específico.
    """
    root = tk.Tk()
    root.withdraw()
    
    current_directory = os.getcwd()
    os.chdir(directory)
    
    file_path = filedialog.askopenfilename(initialdir=directory, title="Seleccione un archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    
    os.chdir(current_directory)
    
    return file_path

def save_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

def create_new_file(user_dir, root_window):
    """
    Función para crear un nuevo archivo de texto.
    """
    ensure_directory_exists(user_dir)
    
    def save_new_file():
        file_name = file_name_entry.get()
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = os.path.join(user_dir, file_name)
        content = text_area.get("1.0", tk.END)
        save_file(file_path, content)
        new_file_window.destroy()
    
    new_file_window = tk.Toplevel(root_window)
    new_file_window.title("Nuevo Archivo de Texto")
    
    file_name_label = tk.Label(new_file_window, text="Nombre del archivo:")
    file_name_label.pack()
    file_name_entry = tk.Entry(new_file_window)
    file_name_entry.pack()
    
    text_area = scrolledtext.ScrolledText(new_file_window, width=40, height=10)
    text_area.pack(fill=tk.BOTH, expand=True)
    
    save_button = tk.Button(new_file_window, text="Guardar", command=save_new_file)
    save_button.pack()
    
    new_file_window.transient(root_window)
    new_file_window.grab_set()
    new_file_window.lift()
    
    new_file_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Editor de Archivos de Texto")
    
    user_dir = os.path.abspath("usuarios/usuario_prueba")
    ensure_directory_exists(user_dir)
    
    open_button = tk.Button(root, text="Abrir Archivo", command=lambda: edit_file(user_dir, root))
    open_button.pack(pady=10)
    
    new_file_button = tk.Button(root, text="Nuevo Archivo", command=lambda: create_new_file(user_dir, root))
    new_file_button.pack(pady=10)
    
    root.mainloop()