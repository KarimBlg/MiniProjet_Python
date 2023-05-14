class AppointmentManager:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def remove_appointment(self, appointment):
        self.appointments.remove(appointment)

    def get_all_appointments(self):
        return self.appointments
    
    def get_appointment(self, index):
        if index < len(self.appointments):
            return self.appointments[index]
        else:
            return None
