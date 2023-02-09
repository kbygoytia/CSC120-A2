# Import all of the information from the computer class so that the two files communicate with each other.
from computer import *

# Import a few useful containers from the typing module
from typing import Dict 

class ResaleShop:

    # What attributes will it need?
    '''inventory: dict = {} 
    itemID: int = 0'''

    # How will you set up your constructor?
    ''' First I will use def __init__(self) and add the attributes inventory and itemID as arguments. This way I can know what itemID belongs to each manually inputed computer and have an inventory to put the computer into.'''

     # What methods will you need?
    ''' buy(), print_inventory(), sell()'''
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, inventory: dict, itemID: int):
        self.inventory = inventory
        self.itemID = 0

    # Everytime a computer is created it will be bought by this function and given an itemID or key value. This key value with the data of the computer will be stored in the resale shop's invetory and assigned to the object computer. 
    def buy(self, computer: Computer):
        self.itemID += 1
        self.inventory[self.itemID] = computer
        return self.itemID

    #This fucntion will go into the resale shop's inventory and input the itemID or key that will extract the data of the assigned value or computer. It will print each piece of information in the value based on the key and the method which calls on the attributes found in the computer class. 
    def print_inventory(self):
         if self.inventory:
            for self.itemID in self.inventory:
                print(f'Item ID: {self.itemID} - {self.inventory[self.itemID].brand}, {self.inventory[self.itemID].processor}, {self.inventory[self.itemID].hard_drive_capacity}, {self.inventory[self.itemID].memory}, {self.inventory[self.itemID].operating_system}, {self.inventory[self.itemID].year_made}, {self.inventory[self.itemID].price}')
         else:
            print("No inventory to display.")
    # This function will take the computer object created in the buy function and identify if the itemID or key is found in the inventory. If it is found then it will delete that computer (key and value) from the inventory and state that it has been sold or if the key does not exist in the function then it will state that it does not exist. 
    def sell(self, computer: Computer):
        if self.itemID in self.inventory:
            del self.inventory[self.itemID]
            print(f"{self.itemID} has been sold!")
        else: 
            print(f"Item {self.itemID} not found. Please select another item to sell.")
def main():
    # First, let's make a computer
    # start = True
    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    # while start: 
    computer_1 = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
    computer_2 = Computer("Mac Air (Late 2015)","3.5 GHc 6-Core Intel Xeon E5",1024, 64, "macOS Big Sur", 2000, 1500)

    # # Add it to the resale store's inventory
    print(f"Buying {computer_2.brand}")
    object_1 = ResaleShop({}, 0)
    print("Adding to inventory...")
    object_1.buy(computer_1)
    object_1.buy(computer_2)
    print("Done.\n")
    
    # Make sure it worked by checking inventory
    print("\n Checking inventory...")
    object_1.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    newOS = "MacOS Monterey"
    print("Refurbishing Item ID:", object_1.itemID, ", updating OS to", newOS)
    print("Updating inventory...")
    computer_1.refurbish()
    computer_1.updateOS(newOS)
    computer_2.refurbish()
    computer_2.updateOS(newOS)
    print("Done.\n")
# 
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    object_1.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print(f'Selling Item ID: {object_1.itemID}')
    object_1.sell(computer_2.brand)
    
    #Make sure it worked by checking inventory.
    print("Checking inventory...")
    object_1.print_inventory()
    print("Done.\n")

main()