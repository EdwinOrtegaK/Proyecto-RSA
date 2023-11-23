import tkinter as tk
from tkinter import ttk, messagebox

class SistemaRSA:
    def __init__(self, root):
        self.root = root
        root.title("RSA Sistema")

        # Mensaje de bienvenida y descripción
        welcome_label = ttk.Label(root, text="Bienvenido al Sistema RSA", font=("Arial", 16))
        welcome_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        description_label = ttk.Label(root, text="¿Qué desea realizar con este sistema: \nencriptar o desencriptar un mensaje?", font=("Arial", 12))
        description_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # Botones para encriptar y desencriptar
        ttk.Button(root, text="Encriptar", command=self.open_encrypt_window).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(root, text="Desencriptar", command=self.open_decrypt_window).grid(row=2, column=1, padx=10, pady=10)

    def open_encrypt_window(self):
        encrypt_window = tk.Toplevel(self.root)
        encrypt_window.title("Encriptador RSA")

        # Widgets para encriptación en encrypt_window
        tk.Label(encrypt_window, text="Mensaje:").grid(row=0, column=0, sticky="w")
        message_entry = ttk.Entry(encrypt_window, width=50)
        message_entry.grid(row=0, column=1)

        tk.Label(encrypt_window, text="p (primo):").grid(row=1, column=0, sticky="w")
        p_entry = ttk.Entry(encrypt_window, width=20)
        p_entry.grid(row=1, column=1)

        tk.Label(encrypt_window, text="q (primo):").grid(row=2, column=0, sticky="w")
        q_entry = ttk.Entry(encrypt_window, width=20)
        q_entry.grid(row=2, column=1)

        tk.Label(encrypt_window, text="e (entero > 1 y coprimo con φ):").grid(row=3, column=0, sticky="w")
        e_entry = ttk.Entry(encrypt_window, width=20)
        e_entry.grid(row=3, column=1)

        # Botón para encriptar
        encrypt_button = ttk.Button(encrypt_window, text="Encriptar", 
                                    command=lambda: self.encrypt_message(message_entry, p_entry, q_entry, e_entry))
        encrypt_button.grid(row=4, column=0, columnspan=2)

    def encrypt_message(self, message_entry, p_entry, q_entry, e_entry):
        try:
            # Obteniendo los valores de entrada
            message = message_entry.get()
            p = int(p_entry.get())
            q = int(q_entry.get())
            e = int(e_entry.get())
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
            encrypted_message = [format(pow(block, e, n), '04d') for block in blocks]

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

    def open_decrypt_window(self):
        decrypt_window = tk.Toplevel(self.root)
        decrypt_window.title("Desencriptador RSA")

        # Widgets para desencriptación en decrypt_window
        tk.Label(decrypt_window, text="Mensaje Cifrado:").grid(row=0, column=0, sticky="w")
        cipher_entry = ttk.Entry(decrypt_window, width=50)
        cipher_entry.grid(row=0, column=1)

        tk.Label(decrypt_window, text="n:").grid(row=1, column=0, sticky="w")
        n_entry = ttk.Entry(decrypt_window, width=20)
        n_entry.grid(row=1, column=1)

        tk.Label(decrypt_window, text="e:").grid(row=2, column=0, sticky="w")
        e_entry = ttk.Entry(decrypt_window, width=20)
        e_entry.grid(row=2, column=1)

        # Botón para desencriptar
        decrypt_button = ttk.Button(decrypt_window, text="Desencriptar", 
                                    command=lambda: self.decrypt_message(cipher_entry, n_entry, e_entry))
        decrypt_button.grid(row=3, column=0, columnspan=2)

    def decrypt_message(self, cipher_entry, n_entry, e_entry):
        try:
            # Obteniendo los valores de entrada
            cipher_text = [int(block) for block in cipher_entry.get().split()]
            n = int(n_entry.get())
            e = int(e_entry.get())

            # Calcular la clave privada d
            phi = self.find_phi(n)  # Implementar esta función para encontrar phi
            d = self.modinv(e, phi)

            # Desencriptar cada bloque
            decrypted_blocks = [pow(c, d, n) for c in cipher_text]

            # Convertir los números desencriptados a letras usando la codificación A→00, B→01, ..., Z→25
            decrypted_message = ''.join([chr(block // 100 + ord('A')) + chr(block % 100 + ord('A')) for block in decrypted_blocks])

            # Mostrar el mensaje desencriptado y la clave privada d en el mismo mensaje
            messagebox.showinfo("Resultado de Desencriptación", f"Mensaje Desencriptado: {decrypted_message}\nClave Privada d: {d}")
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida")

    def modinv(self, a, m):
        # Algoritmo extendido de Euclides para encontrar el inverso multiplicativo
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('No existe inverso modular para %d mod %d' % (a, m))
        else:
            return x % m

    def egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.egcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def find_phi(self, n):
        # En un escenario real, encontrar p y q a partir de n es difícil,
        # pero aquí asumiremos que conocemos p y q
        # p y q deberían ser atributos de la clase o pasarse como argumentos
        p, q = self.find_factors(n) # Implementa esta función si es posible
        return (p - 1) * (q - 1)

    def find_factors(self, n):
        # Esta es una función muy básica para encontrar factores primos.
        # Solo es efectiva para números pequeños.
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i, n // i
        return n, 1  # Si n es primo

# Crear la ventana principal
root = tk.Tk()
app = SistemaRSA(root)

# Ejecutar la aplicación
root.mainloop()