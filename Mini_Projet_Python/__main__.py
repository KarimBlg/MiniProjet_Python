import tkinter as tk
from appointment_app import AppointmentApp

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestionnaire de rendez-vous")
app = AppointmentApp(root)
root.mainloop()


