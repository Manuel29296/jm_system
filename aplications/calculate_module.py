import tkinter as tk

# Función para añadir un número o un operador al display
def add_to_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + value)

# Función para calcular el resultado
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        print("Error:", e)
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Función para borrar el contenido del display
def clear_display():
    display.delete(0, tk.END)

# Función para iniciar la calculadora
def start_calculate():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Calculadora")

    # Crear el display
    global display
    display = tk.Entry(root, width=30, justify="right")
    display.grid(row=0, column=0, columnspan=4)

    # Crear botones numéricos
    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "+"
    ]

    for i, button in enumerate(buttons):
        row = i // 4 + 1
        col = i % 4
        tk.Button(root, text=button, command=lambda button=button: add_to_display(button)).grid(row=row, column=col)

    # Botón de igual
    tk.Button(root, text="=", command=calculate).grid(row=5, column=0, columnspan=2)

    # Botón de borrar
    tk.Button(root, text="C", command=clear_display).grid(row=5, column=2, columnspan=2)

    # Ejecutar el bucle de eventos de la ventana
    root.mainloop()

# Iniciar la calculadora
if __name__ == "__main__":
    start_calculate()