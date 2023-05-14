import tkinter as tk
from tkinter import messagebox
from appointment import Appointment
from appointment_manager import AppointmentManager

class AppointmentApp:
    def __init__(self, root):
        self.root = root
        self.appointment_manager = AppointmentManager()
        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self.root, text="Gestionnaire de rendez-vous", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=10)

        self.label_date = tk.Label(self.root, text="Date:")
        self.label_date.pack()
        self.entry_date = tk.Entry(self.root)
        self.entry_date.pack()

        self.label_time = tk.Label(self.root, text="Heure:")
        self.label_time.pack()
        self.entry_time = tk.Entry(self.root)
        self.entry_time.pack()

        self.label_description = tk.Label(self.root, text="Description:")
        self.label_description.pack()
        self.entry_description = tk.Entry(self.root, width=40)
        self.entry_description.pack()

        self.button_add = tk.Button(self.root, text="Ajouter", command=self.add_appointment)
        self.button_add.pack()

        self.listbox_appointments = tk.Listbox(self.root, width=40, height=10)
        self.listbox_appointments.pack()

        self.button_edit = tk.Button(self.root, text="Modifier", command=self.edit_selected_appointment)
        self.button_edit.pack()

        self.button_remove = tk.Button(self.root, text="Supprimer", command=self.remove_appointment)
        self.button_remove.pack()

        self.refresh_appointments()

        self.frame = tk.Frame(self.root, bd=1, relief=tk.SUNKEN)
        self.frame.pack(side=tk.BOTTOM)

        self.label = tk.Label(self.frame, text="Réalisé par BOUALLAG Karim", fg="red")
        self.label.pack(padx=10, pady=5)

    def refresh_appointments(self):
        self.listbox_appointments.delete(0, tk.END)
        appointments = self.appointment_manager.get_all_appointments()
        for appointment in appointments:
            self.listbox_appointments.insert(tk.END, str(appointment))

    def add_appointment(self):
        date = self.entry_date.get()
        time = self.entry_time.get()
        description = self.entry_description.get()
        if date and time and description:
            appointment = Appointment(date, time, description)
            self.appointment_manager.add_appointment(appointment)
            self.refresh_appointments()
            self.entry_date.delete(0, tk.END)
            self.entry_time.delete(0, tk.END)
            self.entry_description.delete(0, tk.END)
        else:
            messagebox.showerror("Erreur", "Veuillez saisir tous les champs du rendez-vous.")
    
    def edit_selected_appointment(self):
        selected_index = self.listbox_appointments.curselection()
        if selected_index:
           selected_appointment = self.appointment_manager.get_appointment(selected_index)


    def remove_appointment(self):
        selection = self.listbox_appointments.curselection()
        if selection:
            index = selection[0]
            appointment = self.appointment_manager.get_all_appointments()[index]
            self.appointment_manager.remove_appointment(appointment)
            self.refresh_appointments()
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un rendez-vous.")

