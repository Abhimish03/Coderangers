import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
# Normally, you would save this key securely and reuse it
key = Fernet.generate_key()
cipher_suite = Fernet(key)

class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptography GUI")
        
        self.input_label = tk.Label(root, text="Enter text to encrypt/decrypt:")
        self.input_label.pack()

        self.input_text = tk.Text(root, height=10, width=50)
        self.input_text.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack()

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def encrypt(self):
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            if not text:
                raise ValueError("Input text is empty")
            encrypted_text = cipher_suite.encrypt(text.encode())
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, encrypted_text.decode())
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            if not text:
                raise ValueError("Input text is empty")
            decrypted_text = cipher_suite.decrypt(text.encode())
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, decrypted_text.decode())
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()
