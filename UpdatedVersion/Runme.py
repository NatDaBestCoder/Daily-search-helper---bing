import tkinter as tk
import settings
def run_program():
    import BingPoints

def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    
    tk.Label(settings_window, text="Enter Command To Web Browser:").pack()
    entry1 = tk.Entry(settings_window)
    entry1.pack()
    entry1.bind("<Return>", lambda event: set_value1(entry1))
    
    tk.Label(settings_window, text="Enter Value 2:").pack()
    entry2 = tk.Entry(settings_window)
    entry2.pack()
    entry2.bind("<Return>", lambda event: set_value2(entry2))

def set_value1(entry):
    settings.command = entry.get()
    print(f"Value 1 set to: {settings.command}")

def set_value2(entry):
    value2 = entry.get()
    print(f"Value 2 set to: {value2}")



root = tk.Tk()
root.title("Main Window")

run_button = tk.Button(root, text="Run Program", command=run_program)
run_button.pack(pady=10)

settings_button = tk.Button(root, text="Open Settings", command=open_settings)
settings_button.pack(pady=10)

root.mainloop()
