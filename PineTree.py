import subprocess
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

seven_zip_path = "C:/Program Files/7-zip/7z.exe"

# Check if 7-Zip exists, otherwise show an error and exit
if not os.path.exists(seven_zip_path):
    messagebox.showerror("Error", "This application requires 7-Zip to extract files. Please download 7-Zip from the official website.")
    exit()

def browse_source():
    file_path = filedialog.askopenfilename(title="Select a file to extract")
    source_entry.delete(0, tk.END)
    source_entry.insert(0, file_path)

def browse_output():
    folder_path = filedialog.askdirectory(title="Select output folder")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, folder_path)

def extract_files():
    source = source_entry.get()
    output = output_entry.get()
    
    if not source or not output:
        messagebox.showerror("Error", "Please provide both source file and output folder.")
        return
    
    try:
        command = [seven_zip_path, "x", source, f"-o{output}", "-y"]
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", "Extraction completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Extraction failed: {e}")

# Create the main window
root = tk.Tk()
root.title("PineTree")
root.geometry("583x144")
root.resizable(False, False)
root.iconbitmap("icon.ico")

# UI Elements
frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Source File:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
source_entry = ttk.Entry(frame, width=60)
source_entry.grid(row=0, column=1, padx=5, pady=5)
source_btn = ttk.Button(frame, text="Browse", command=browse_source)
source_btn.grid(row=0, column=2, padx=5, pady=5)

ttk.Label(frame, text="Output Folder:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
output_entry = ttk.Entry(frame, width=60)
output_entry.grid(row=1, column=1, padx=5, pady=5)
output_btn = ttk.Button(frame, text="Browse", command=browse_output)
output_btn.grid(row=1, column=2, padx=5, pady=5)

extract_btn = ttk.Button(frame, text="Extract", command=extract_files)
extract_btn.grid(row=2, column=1, pady=10)

# Run the app
root.mainloop()