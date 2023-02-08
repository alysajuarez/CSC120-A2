class Computer:


    # What attributes will it need?

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int



    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    """
    setting attributes for creating computer
    """
    def __init__(self, description, processor, capacity, mem, os, year, amount):
        self.description = description
        self.processor_type = processor
        self.hard_drive_capacity = capacity
        self.memory = mem
        self.operating_system = os 
        self.year_made = year
        self.price = amount
        
    # What methods will you need?

    """
    takes in new price and updates price of computer
    """
    def update_price(self, new_amount):
        self.price = new_amount

    """
    takes in new operating system and updates operating system of computer
    """
    def update_os(self, new_os):
        self.operating_system = new_os