class Car(object):
    def __init__(self, name, color, model, company, speed_limit):
        self.name = name
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped") 

    def accelerate(self):
        print("accelerating")
        "accelerating"

    def change_gear(self, gear_type):
        print("gear changed")
        "gear related function"
    
bugatti = Car("chiron", "black", "a43rt", "bugatti", "304.733mph")

print(bugatti.start()) 
print(bugatti.color)
print(bugatti.model)
print(bugatti.company)