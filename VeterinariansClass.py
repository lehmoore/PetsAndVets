class Vets():

    def __init__(self, name, phone, email, location, specialty):
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location
        self.specialty = specialty

    def patient(self):
       return "This patient is cured! Off you go"