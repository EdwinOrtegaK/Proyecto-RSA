import tkinter as tk
from tkinter import ttk, messagebox

class SistemaRSA:
    def __init__(self, root):
        self.root = root
        root.title("RSA Encriptador/Desencriptador")

        # Utilizando ttk para una mejor apariencia de los widgets
        tk.Label(root, text="Mensaje:").grid(row=0, column=0, sticky="w")
        self.message_entry = ttk.Entry(root, width=50)
        self.message_entry.grid(row=0, column=1)

        tk.Label(root, text="p (primo):").grid(row=1, column=0, sticky="w")
        self.p_entry = ttk.Entry(root, width=20)
        self.p_entry.grid(row=1, column=1)

        tk.Label(root, text="q (primo):").grid(row=2, column=0, sticky="w")
        self.q_entry = ttk.Entry(root, width=20)
        self.q_entry.grid(row=2, column=1)

        tk.Label(root, text="e (entero > 1 y coprimo con φ):").grid(row=3, column=0, sticky="w")
        self.e_entry = ttk.Entry(root, width=20)
        self.e_entry.grid(row=3, column=1)

        # Botones para encriptar y desencriptar
        encrypt_button = ttk.Button(root, text="Encriptar", command=self.encrypt_message)
        encrypt_button.grid(row=4, column=0)

        decrypt_button = ttk.Button(root, text="Desencriptar", command=self.decrypt_message)
        decrypt_button.grid(row=4, column=1)

    def encrypt_message(self):
        try:
            # Obteniendo los valores de entrada
            message = self.message_entry.get()
            p = int(self.p_entry.get())
            q = int(self.q_entry.get())
            e = int(self.e_entry.get())
            n = p * q
            phi = (p - 1) * (q - 1)

            # Verificar que e sea mayor que 1 y coprimo con φ
            if e <= 1 or not self.is_coprime(e, phi):
                messagebox.showerror("Error", "e debe ser mayor que 1 y coprimo con φ")
                return

            # Codificación A→00, B→01, ..., Z→25 y agrupar en bloques de 2 letras
            number_message = ''.join([format(ord(char.upper()) - ord('A'), '02d') 
                                      for char in message if char.isalpha()])
            blocks = [int(number_message[i:i+4]) for i in range(0, len(number_message), 4)]

            # Encriptar cada bloque
            encrypted_message = [str(pow(block, e, n)) for block in blocks]

            # Mostrar el mensaje encriptado
            messagebox.showinfo("Mensaje Encriptado", ' '.join(encrypted_message))
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida")

    def is_coprime(self, a, b):
        return self.gcd(a, b) == 1

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def decrypt_message(self):
        # Aquí se implementará la lógica de desencriptación
        messagebox.showinfo("Desencriptar", "Desencriptando mensaje... (Esta parte se implementará)")

# Crear la ventana principal
root = tk.Tk()
app = SistemaRSA(root)

# Ejecutar la aplicación
root.mainloop()