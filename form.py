import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    
    if name and email and password:
        messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}")
    else:
        messagebox.showwarning("Incomplete Form", "Please fill in all fields.")

# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x200")

# Labels and Entry fields
tk.Label(root, text="Name").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Email").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.pack(pady=10)

# Run the application
root.mainloop()