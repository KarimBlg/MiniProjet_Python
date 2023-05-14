class Appointment:
    def __init__(self, date, time, description):
        self.date = date
        self.time = time
        self.description = description

    def __str__(self):
        return f"{self.date} à {self.time}: {self.description}"
