import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files(files, directory):
    for file in files:
        file_extension = file.split('.')[-1].lower()
        folder_name = file_extension
        folder_path = os.path.join(directory, folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        shutil.move(file, os.path.join(folder_path, os.path.basename(file)))

def upload_files():
    files = filedialog.askopenfilenames(title="Select files to upload")
    
    if files:
        folder_path = filedialog.askdirectory(title="Select target folder")
        
        if folder_path:
            try:
                organize_files(files, folder_path)
                messagebox.showinfo("Success", "Files organized successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "No target folder selected!")
    else:
        messagebox.showwarning("Warning", "No files selected!")

root = tk.Tk()
root.title("File Organizer")

root.geometry("300x200")

label = tk.Label(root, text="Click below to upload files and organize them", pady=20)
label.pack()
upload_button = tk.Button(root, text="Click here to upload files", command=upload_files)
upload_button.pack(pady=10)
root.mainloop()
