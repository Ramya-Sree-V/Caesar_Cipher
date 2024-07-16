from tkinter import *
from tkinter import messagebox

def caesar_encrypt(text, shift):
    """Encrypts text using the Caesar Cipher with a given shift."""
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_decrypt(text, shift):
    """Decrypts text using the Caesar Cipher with a given shift."""
    return caesar_encrypt(text, -shift)

def encrypt_message():
    message = entry_message.get(1.0, END).strip()
    try:
        shift = int(entry_shift.get(1.0, END).strip())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer shift value.")
        return
    result = caesar_encrypt(message, shift)
    text_result.config(state=NORMAL)
    text_result.delete(1.0, END)
    text_result.insert(END, f"Encrypted message: {result}")
    text_result.config(state=DISABLED)

def decrypt_message():
    message = entry_message.get(1.0, END).strip()
    try:
        shift = int(entry_shift.get(1.0, END).strip())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer shift value.")
        return
    result = caesar_decrypt(message, shift)
    text_result.config(state=NORMAL)
    text_result.delete(1.0, END)
    text_result.insert(END, f"Decrypted message: {result}")
    text_result.config(state=DISABLED)

# GUI Setup
root = Tk()
root.geometry("410x350")
root.title("Caesar Cipher Tool")
root.config(background ='#16537e',borderwidth=1.5, relief="solid")


Label(root, text="Enter Message:",borderwidth=1.5, relief="solid").place(x=170, y=23)
entry_message = Text(root, height=5, width=40,borderwidth=1.5, relief="solid")
entry_message.place(x=50, y=50)

Label(root, text="Enter Shift:",borderwidth=1.5, relief="solid").place(x=50, y=140)
entry_shift = Text(root, height=1, width=10,borderwidth=1.5, relief="solid")
entry_shift.place(x=120, y=140)

b1 = Button(root, text="Encrypt", command=encrypt_message,borderwidth=1.5, relief="solid")
b1.place(x=50, y=185)

b2 = Button(root, text="Decrypt", command=decrypt_message,borderwidth=1.5, relief="solid")
b2.place(x=320, y=185)

text_result = Text(root, height=5, width=40, state=DISABLED,borderwidth=1.5, relief="solid")
text_result.place(x=50, y=220)

root.mainloop()