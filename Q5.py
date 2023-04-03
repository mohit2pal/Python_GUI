#Question 5

import tkinter as tk
window = tk.Tk()
window.title("Contact Section")
contacts = []
def add_contact():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    contacts.append((first_name, last_name, email, phone))
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    update_contact_list()
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact[0]} {contact[1]}")
contact_section = tk.Frame(window)
contact_section.pack()
first_name_label = tk.Label(contact_section, text="First Name:")
first_name_label.grid(row=0, column=0, padx=10, pady=10)
first_name_entry = tk.Entry(contact_section)
first_name_entry.grid(row=0, column=1, padx=10, pady=10)
last_name_label = tk.Label(contact_section, text="Last Name:")
last_name_label.grid(row=1, column=0, padx=10, pady=10)
last_name_entry = tk.Entry(contact_section)
last_name_entry.grid(row=1, column=1, padx=10, pady=10)
email_label = tk.Label(contact_section, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=10)
email_entry = tk.Entry(contact_section)
email_entry.grid(row=2, column=1, padx=10, pady=10)
phone_label = tk.Label(contact_section, text="Phone:")
phone_label.grid(row=3, column=0, padx=10, pady=10)
phone_entry = tk.Entry(contact_section)
phone_entry.grid(row=3, column=1, padx=10, pady=10)
submit_button = tk.Button(contact_section, text="Submit", command=add_contact)
submit_button.grid(row=4, column=0, padx=10, pady=10)
clear_button = tk.Button(contact_section, text="Clear", command=lambda:
(first_name_entry.delete(0, tk.END), last_name_entry.delete(0, tk.END),
email_entry.delete(0, tk.END), phone_entry.delete(0, tk.END)))
clear_button.grid(row=4, column=1, padx=10, pady=10)
contact_list = tk.Listbox(window)
contact_list.pack()
window.mainloop()
