
# Base Class for Laptop Information and Status
class LaptopInfos:
    def __init__(self, laptop_id, laptop_status):
        
        # Attributes
        self.laptop_id = laptop_id
        self.laptop_status = laptop_status

        # call the methods here
        self.update_status()
        self.display_laptop_info()

    # Method to update laptop status
    def update_status(self):

        # here instead of print pass it to a class that process the rental 
        print(f"Laptop {self.laptop_id} status updated to {self.laptop_status}")

    # Method to display laptop info
    def display_laptop_info(self):
        print(f"Laptop ID: {self.laptop_id}, Status: {self.laptop_status}")