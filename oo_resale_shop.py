from computer import *

class ResaleShop:

    # What attributes will it need?

    inventory:list # list of computer objects

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    """
    setting attributes for store 
    """
    def __init__(self, computer):
        self.inventory = []


    # What methods will you need?

    """
    takes in details of a computer and adds the computer to inventory
    """
    def buy (self, description, processor, capacity, mem, os, year, amount):
         # call Computer(...) constructor - to create new computer instance
        computer = Computer(description, processor, capacity, mem, os, year, amount)
        # call inventory.append (...) - to add the new computer instance to inventory
        self.inventory.append(computer)


    """
    finds computer in inventory and removes computer if it exists in inventory
    """
    def sell(self, computer):
        # need to find specific computer
        if computer in self.inventory:
        # call inventory.remove(...) - to remove computer from inventory
            self.inventory.remove(computer)
        else: 
            print(computer, "not found. please select another item to sell.")


    """
    takes in a new operating system and raises price according to year made
    """
    def refurbish(self, computer, new_os):
        if computer in self.inventory:
            if computer.year_made < 2000:
                computer.price = 0 # too old to sell, donation only
            elif computer.year_made < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff
            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print(computer, "not found. please select another item to refurbish.")
        
    

"""
test space for program
"""
def main():
        # Computer is the contructor
        computer1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2019, 500)
        computer2 = Computer("MacBook Air (2017)", "1.8GHz Core i5", 256, 8, "macOS 10.12 Sierra", 2017, 650)
        print(computer1.description)

        myStore = ResaleShop(computer1)
        myStore.buy("MacBook Pro 13.3 Touch Bar (2019)", "Intel Core i7 2.8GHz", 512, 16, "macOS 10.15 Catalina", 2019, 800)
    
        # variable points to computer instance
        
        print(computer1.price)
        computer1.update_price(600)
        print(computer1.price)

        print(computer1.operating_system)
        computer1.update_os("macOS 13.1")
        print(computer1.operating_system)

        myStore.refurbish(computer2, "new os")
        print(computer2.price)
        print(computer2.operating_system)

        myStore.sell(computer2)



main()



