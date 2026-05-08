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


