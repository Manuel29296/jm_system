import tkinter as tk
import webbrowser

def open_browser():
    # URL a la que se abrirá el navegador
    url = "https://www.google.com"
    
    # Abrir el navegador web con la URL especificada
    webbrowser.open(url)

def open_browser_from_application():
    # Crear una ventana de Tkinter para el navegador
    browser_window = tk.Toplevel()
    browser_window.title("Navegador")

    # Botón para abrir el navegador
    open_button = tk.Button(browser_window, text="Abrir Navegador", command=open_browser)
    open_button.pack(pady=10)

    # Ejecutar la aplicación del navegador
    browser_window.mainloop()