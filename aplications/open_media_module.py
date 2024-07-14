import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os

def open_media_viewer():
    root = tk.Tk()
    root.title("Media Viewer")

    def open_media():
        current_dir = os.getcwd()
        file_path = filedialog.askopenfilename(initialdir=current_dir, filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg"), ("Archivos de video", "*.mp4;*.avi")])
        print("File selected:", file_path)  # Imprimir la ruta seleccionada
        if file_path:
            try:
                if os.path.exists(file_path):  # Verificar si el archivo existe
                    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                        image = Image.open(file_path)
                        photo = ImageTk.PhotoImage(image)
                        label.config(image=photo)
                        label.image = photo
                    elif file_path.lower().endswith(('.mp4', '.avi')):
                        cap = cv2.VideoCapture(file_path)
                        ret, frame = cap.read()
                        if ret:
                            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            image = Image.fromarray(cv2image)
                            photo = ImageTk.PhotoImage(image)
                            label.config(image=photo)
                            label.image = photo
                        else:
                            messagebox.showerror("Error", "No se pudo cargar el video")
                else:
                    messagebox.showerror("Error", "El archivo seleccionado no existe")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")

    button_open = tk.Button(root, text="Abrir Archivo", command=open_media)
    button_open.pack(pady=10)

    label = tk.Label(root)
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    open_media_viewer()