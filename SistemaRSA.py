import tkinter as tk
from tkinter import messagebox

class SistemaRSA:
    def __init__(self, root):
        self.root = root
        root.title("Sistema RSA Encriptador/Desencriptador")

        # Etiquetas y campos de entrada para los datos
        tk.Label(root, text="Mensaje:").grid(row=0, column=0)
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.grid(row=0, column=1)

        tk.Label(root, text="p (primo):").grid(row=1, column=0)
        self.p_entry = tk.Entry(root, width=20)
        self.p_entry.grid(row=1, column=1)

        tk.Label(root, text="q (primo):").grid(row=2, column=0)
        self.q_entry = tk.Entry(root, width=20)
        self.q_entry.grid(row=2, column=1)

        tk.Label(root, text="e (entero):").grid(row=3, column=0)
        self.e_entry = tk.Entry(root, width=20)
        self.e_entry.grid(row=3, column=1)

        # Botones para encriptar y desencriptar
        encrypt_button = tk.Button(root, text="Encriptar", command=self.encrypt_message)
        encrypt_button.grid(row=4, column=0)

        decrypt_button = tk.Button(root, text="Desencriptar", command=self.decrypt_message)
        decrypt_button.grid(row=4, column=1)

    def encrypt_message(self):
        # Aquí se implementará la lógica de encriptación
        messagebox.showinfo("Encriptar", "Encriptando mensaje... (Esta parte se implementará)")

    def decrypt_message(self):
        # Aquí se implementará la lógica de desencriptación
        messagebox.showinfo("Desencriptar", "Desencriptando mensaje... (Esta parte se implementará)")

# Crear la ventana principal
root = tk.Tk()
app = SistemaRSA(root)

# Ejecutar la aplicación
root.mainloop()