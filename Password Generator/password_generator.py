import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Oops! Select at least one option."
    
    return "".join(random.choice(characters) for _ in range(length))

def generate_and_display():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Uh-oh", "Password should be at least 4 characters long.")
            return
        
        password = generate_password(
            length,
            letters_var.get(),
            numbers_var.get(),
            symbols_var.get()
        )
        
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Oops", "Enter a valid number for length.")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success!", "Password copied to clipboard.")
    else:
        messagebox.showerror("Error", "There's nothing to copy!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

tk.Label(root, text="Choose Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols (!@#$...)", variable=symbols_var).pack()

generate_btn = tk.Button(root, text="Generate Password", command=generate_and_display)
generate_btn.pack()

password_entry = tk.Entry(root, width=30)
password_entry.pack()

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack()

root.mainloop()
