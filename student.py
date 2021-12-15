# Module of what a student is

class Student:
    #defining what a student data is; values are actually in classes_objects file
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


# Honor roll object function to check if on honorroll
def on_honor_roll(self):
    if self.gpa >= 3.5:
        return True
    else:
        return False