import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import threading
import main

def run_script():
    file1 = file1_entry.get()
    file2 = file2_entry.get()
    output_folder = output_entry.get()

    # Validate the selected paths
    if not (os.path.isfile(file1) and os.path.isfile(file2)):
        messagebox.showerror("Error", "Please select valid input files.")
        return
    if not os.path.isdir(output_folder):
        messagebox.showerror("Error", "Please select a valid output folder.")
        return

    # Hide the "Comparar" button and show the progress bar
    output_button.grid_remove() 
    progress_bar.grid(row=4, column=1, padx=10, pady=20)  # Show the progress bar
    progress_bar.start()  
    siia_button.config(state=tk.DISABLED)
    ch_button.config(state=tk.DISABLED)
    save_button.config(state=tk.DISABLED)

    # Run the script in a separate thread to avoid freezing the UI
    threading.Thread(target=execute_script, args=(file1, file2, output_folder)).start()

def execute_script(file1, file2, output_folder):
    try:
        # Run your script and capture the output
        result = main.run_script(file1, file2, output_folder)
        if result['success']:
            messagebox.showinfo("Success", "Script executed successfully!")
        else:            
            messagebox.showerror("Error", f"Script success: {result['success']}\n{result['error']}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        # Stop the progress bar, hide it, and show the "Comparar" button again
        progress_bar.stop()
        progress_bar.grid_remove() 
        output_button.grid(row=5, column=1, padx=10, pady=20)  # Show the "Comparar" button
        siia_button.config(state=tk.NORMAL)
        ch_button.config(state=tk.NORMAL)
        save_button.config(state=tk.NORMAL)

def select_file1():
    file_path = filedialog.askopenfilename()
    file1_entry.delete(0, tk.END)
    file1_entry.insert(0, file_path)

def select_file2():
    file_path = filedialog.askopenfilename()
    file2_entry.delete(0, tk.END)
    file2_entry.insert(0, file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, folder_path)

# hoover
def on_enter(e):
    output_button['background'] = '#1070c9'

def on_leave(e):
    output_button['background'] = '#05549D'

# Create the main window
root = tk.Tk()
root.title("ComparacionCD")
root.configure(bg='white', padx=10, pady=10)

# Apply modern style using ttk
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), background="white")
style.configure("TLabel", font=("Helvetica", 12), background="white")
style.configure("TEntry", font=("Helvetica", 12), padding=5)

# Cargar la imagen PNG usando Pillow
image = Image.open("assets/iconcd_name.ico")  # Asegúrate de que la ruta sea correcta
image = image.resize((70,70), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(root, image=photo, bg="white")  # El fondo del Label es blanco
label_image.grid(row=0, column=0, padx=5, pady=5)
# Mantener una referencia a la imagen para evitar la recolección de basura
label_image.image = photo

image2 = Image.open("assets/logouaq.png")  # Asegúrate de que la ruta sea correcta
image2 = image2.resize((90,46), Image.Resampling.LANCZOS)
photo2 = ImageTk.PhotoImage(image2)
label_image = tk.Label(root, image=photo2, bg="white")  # El fondo del Label es blanco
label_image.grid(row=0, column=2, padx=5, pady=5)
# Mantener una referencia a la imagen para evitar la recolección de basura
label_image.image = photo

# Create labels and entry fields for file selection
ttk.Label(root, text="Archivo SIIA:").grid(row=1, column=0, padx=15, pady=10, sticky=tk.E)
file1_entry = ttk.Entry(root, width=50)
file1_entry.grid(row=1, column=1, padx=10, pady=10)
siia_button = ttk.Button(root, text="Seleccionar", command=select_file1)
siia_button.grid(row=1, column=2, padx=10, pady=10)

ttk.Label(root, text="Archivo CH:").grid(row=2, column=0, padx=15, pady=10, sticky=tk.E)
file2_entry = ttk.Entry(root, width=50)
file2_entry.grid(row=2, column=1, padx=10, pady=10)
ch_button = ttk.Button(root, text="Seleccionar", command=select_file2)
ch_button.grid(row=2, column=2, padx=10, pady=10)

ttk.Label(root, text="Folder de\nGuardado:").grid(row=3, column=0, padx=15, pady=10, sticky=tk.E)
output_entry = ttk.Entry(root, width=50)
output_entry.grid(row=3, column=1, padx=10, pady=10)
save_button = ttk.Button(root, text="Seleccionar", command=select_output_folder)
save_button.grid(row=3, column=2, padx=10, pady=10)

# Create the progress bar (hidden by default)
progress_bar = ttk.Progressbar(root, mode='indeterminate', length=300)
progress_bar.grid(row=4, column=1, padx=10, pady=20)
progress_bar.grid_remove()  # Hide the progress bar initially

output_button = tk.Button(root, text="Comparar",font=("Helvetica", 12, 'bold'), border=0, command=run_script, bg="#05549D", fg="white", width=12)
output_button.grid(row=5, column=1, padx=10, pady=20)
output_button.bind("<Enter>", on_enter)
output_button.bind("<Leave>", on_leave)

# Start the GUI event loop
root.iconbitmap('assets\iconcd.ico')
root.geometry("615x350")
root.resizable(False, False)
root.mainloop()