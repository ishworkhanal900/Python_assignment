"""
    Student class consist of:
            * Name, address, totalmarks, contact, gender s important parameter
            * Company type is set by default to "Software and IT"
            * Maximum Salary, Minimum Salary and Average Salary is non important
              parameters.
            * Investment and Profit Information is also non important parameters
            * Constructor __init__ sets all the important and non important
              parameters.
            * Company Type set up is set by the method set_company_type().
            * Company salary info is set by the method salary_info().
            * Company transaction info is set by the method transaction_info().
            * Whole Company information is printed by print_info() method.
    Testing:
            * c1 object test without salary information which is set to default.
            * c2 object test with all the parameters set.
"""


class Student:
    
    def __init__(self, name, address, totalmarks, contact, gender):
        
        self.name = name
        self.address = address
        self.totalmarks = totalmarks
        self.contact = contact
        self.gender = gender

    def updateMarks(self):
        a = int(input("inter total mark :"))
        self.totalmarks = self.totalmarks + a
        print("New updated marks is :",self.totalmarks)


       

d = Student("Ishwor", "kamaladi",120, "9843089340", "male")

d.updateMarks()

