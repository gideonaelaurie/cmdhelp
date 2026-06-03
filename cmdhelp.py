#!/usr/bin/env python3
# Version 1.2.1 Stable Release
import tkinter as tk
from tkinter import scrolledtext
import subprocess

def search_commands():
    keyword = entry.get().strip()
    if not keyword:
        output_area.delete(1.0, tk.END)
        output_area.insert(tk.INSERT, "Please enter a keyword.")
        return
        
    try:
        # Runs the 'apropos' command and captures output safely
        result = subprocess.check_output(['apropos', keyword], stderr=subprocess.STDOUT).decode('utf-8')
        output_area.delete(1.0, tk.END)
        output_area.insert(tk.INSERT, result)
    except subprocess.CalledProcessError:
        # Handles the error smoothly if no matching commands are found
        output_area.delete(1.0, tk.END)
        output_area.insert(tk.INSERT, f"No commands found for: {keyword}")

# Initialize GUI
root = tk.Tk()
root.title("Linux Command Helper")

# UI Elements
tk.Label(root, text="Search for a command:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
tk.Button(root, text="Find", command=search_commands).pack(pady=5)
output_area = scrolledtext.ScrolledText(root, width=60, height=15)
output_area.pack(padx=10, pady=10)

root.mainloop()

