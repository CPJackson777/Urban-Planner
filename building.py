# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.

# Properties
# designer - It will hold your name.
# date_constructed - This will hold the exact time the building was created.
# owner - This will store the same of the person who owns the building.
# address
# stories
# Methods
# Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

# Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

# Constructor
# Define your __init__ method to accept two arguments

# address
# stories
# Once defined this way, you can send those values as parameters when you create each instance

#  eight_hundred_eighth = Building("800 8th Street", 12)
import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
    
    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, buyer):
        self.owner = buyer

# Creating Your Buildings
# Create 5 building instances
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# Once all buildings are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example
# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.

def print_report(building):
    print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.')

building_one = Building("123 Hello Dr.", 6)
building_one.purchase("Gary")
building_one.construct()
print_report(building_one)

building_two = Building("456 Wassup Rd", 4)
building_two.purchase("Andre")
building_two.construct()
print_report(building_two)

building_three = Building("789 Broham Blvd", 7)
building_three.purchase("Darren")
building_three.construct()
print_report(building_three)

building_four = Building("543 Greetings Ave", 2)
building_four.purchase("Derrick")
building_four.construct()
print_report(building_four)

building_five = Building("777 Morning Dr", 4)
building_five.purchase("Antonio")
building_five.construct()
print_report(building_five)

