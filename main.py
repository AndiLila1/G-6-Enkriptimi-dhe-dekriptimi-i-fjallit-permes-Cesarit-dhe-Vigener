import tkinter as tk
from tkinter import filedialog, messagebox

from caesar import caesar
from vigenere import vigenere


def browse_input_file():
    path = filedialog.askopenfilename(
        title="Select input file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if path:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, path)


def choose_output_file():
    path = filedialog.asksaveasfilename(
        title="Choose output file",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if path:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, path)


def save_message_to_file():
    message = message_text.get("1.0", tk.END).strip()

    if not message:
        messagebox.showerror("Error", "TextBox is empty. Write a message first.")
        return

    path = filedialog.asksaveasfilename(
        title="Save message",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if path:
        with open(path, "w", encoding="utf-8") as file:
            file.write(message)
        messagebox.showinfo("Success", "Message saved successfully.")


def validate_key():
    key = key_entry.get().strip()

    if algorithm_choice.get() == "Caesar Cipher":
        try:
            return int(key)
        except ValueError:
            messagebox.showerror("Error", "Caesar Cipher key must be an integer.")
            return None

    if not key:
        messagebox.showerror("Error", "Vigenere Cipher key must not be empty.")
        return None

    if not any(char.isalpha() for char in key):
        messagebox.showerror("Error", "Vigenere Cipher key must contain letters.")
        return None

    return key