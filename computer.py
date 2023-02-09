class Computer:
# 
    # What attributes will it need?
    '''brand: str = ""
    processor: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    os: str = ""
    year: int = 0
    price: int = 0'''

    # How will you set up your constructor?
    '''First I will use def __init__(self) and add the attributes brand, processor, hard_drive_capacity, memory, operating_system, year_made, and price as arguements. 
    This way I can know for the refurbish method whether a computer is old or new which will determine the price and if it has an OS so that it can be later updated.. 
    If the computer has an old operating system then I will decide whether or not to update it.
    I will also have the computer's brand to help with identifying it inside invetory later on. The other information are attributes I find important to know for computer information which would be used in the real world. 
'''
    # What methods will you need?
    '''refurbish(), updateOS()'''
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, brand: str,  processor: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.brand = brand
        self.processor = processor
        self.hard_drive_capacity= hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

                   
    # Takes in the manually created computer object in resale shop and updates the price based on the year of the object
    def refurbish(self):
        if self.year_made < 2000:
            self.price = 0
        elif self.year_made < 2012:
            self.price = 250
        elif self.year_made < 2018:
            self.price = 550
        else:
            self.price = 1000 

    # Takes in the manually created computer object in resale shop and updates the operating system to MacOS Monterry unless the newOS variable is made equal to None in which case the operating system will stay the same.
    def updateOS(self, newOS: str) -> None:
         if newOS != None:
            self.operating_system = newOS
            return self.operating_system

def main():
        
    ex_1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 1999, 1500)
    ex_1.refurbish()
    print(ex_1.price)

main()