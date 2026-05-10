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


def start_process():
    input_path = input_file_entry.get().strip()
    output_path = output_file_entry.get().strip()
    key = validate_key()

    if not input_path:
        messagebox.showerror("Error", "Please select an input file.")
        return

    if not output_path:
        messagebox.showerror("Error", "Please choose an output file path.")
        return

    if key is None:
        return

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            file_content = file.read()

        if algorithm_choice.get() == "Caesar Cipher":
            if operation_choice.get() == "Encrypt":
                result = caesar.encrypt(file_content, key)
            else:
                result = caesar.decrypt(file_content, key)
        else:
            if operation_choice.get() == "Encrypt":
                result = vigenere.encrypt(file_content, key)
            else:
                result = vigenere.decrypt(file_content, key)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(result)

        messagebox.showinfo("Success", "File processed and saved successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Input file was not found.")
    except OSError as error:
        messagebox.showerror("Error", f"File error: {error}")


root = tk.Tk()
root.title("File Encryption and Decryption using Caesar and Vigenere Algorithms")
root.geometry("760x600")
root.resizable(False, False)
root.configure(bg="#f4f6f8")

algorithm_choice = tk.StringVar(value="Caesar Cipher")
operation_choice = tk.StringVar(value="Encrypt")

title_label = tk.Label(
    root,
    text="File Encryption and Decryption",
    font=("Arial", 18, "bold"),
    bg="#f4f6f8"
)
title_label.pack(pady=15)

main_frame = tk.Frame(root, bg="#f4f6f8")
main_frame.pack(padx=25, fill="both")

tk.Label(main_frame, text="Write a message:", font=("Arial", 11), bg="#f4f6f8").grid(row=0, column=0, sticky="w")
message_text = tk.Text(main_frame, width=75, height=6, font=("Arial", 11))
message_text.grid(row=1, column=0, columnspan=3, pady=5)

save_message_button = tk.Button(main_frame, text="Save TextBox Message to File", width=25, command=save_message_to_file)
save_message_button.grid(row=2, column=0, sticky="w", pady=8)

tk.Label(main_frame, text="Encryption algorithm:", font=("Arial", 11), bg="#f4f6f8").grid(row=3, column=0, sticky="w", pady=(15, 3))
tk.OptionMenu(main_frame, algorithm_choice, "Caesar Cipher", "Vigenere Cipher").grid(row=3, column=1, sticky="w", pady=(15, 3))

tk.Label(main_frame, text="Operation:", font=("Arial", 11), bg="#f4f6f8").grid(row=4, column=0, sticky="w", pady=3)
tk.OptionMenu(main_frame, operation_choice, "Encrypt", "Decrypt").grid(row=4, column=1, sticky="w", pady=3)

tk.Label(main_frame, text="Key:", font=("Arial", 11), bg="#f4f6f8").grid(row=5, column=0, sticky="w", pady=3)
key_entry = tk.Entry(main_frame, width=35, font=("Arial", 11))
key_entry.grid(row=5, column=1, sticky="w", pady=3)

tk.Label(main_frame, text="Input file path:", font=("Arial", 11), bg="#f4f6f8").grid(row=6, column=0, sticky="w", pady=(15, 3))
input_file_entry = tk.Entry(main_frame, width=55, font=("Arial", 10))
input_file_entry.grid(row=6, column=1, pady=(15, 3))
tk.Button(main_frame, text="Browse", width=12, command=browse_input_file).grid(row=6, column=2, padx=8, pady=(15, 3))

tk.Label(main_frame, text="Output file path:", font=("Arial", 11), bg="#f4f6f8").grid(row=7, column=0, sticky="w", pady=3)
output_file_entry = tk.Entry(main_frame, width=55, font=("Arial", 10))
output_file_entry.grid(row=7, column=1, pady=3)
tk.Button(main_frame, text="Choose", width=12, command=choose_output_file).grid(row=7, column=2, padx=8, pady=3)

start_button = tk.Button(
    main_frame,
    text="Start Encryption / Decryption",
    width=28,
    font=("Arial", 11, "bold"),
    command=start_process
)
start_button.grid(row=8, column=0, columnspan=3, pady=25)

root.mainloop()