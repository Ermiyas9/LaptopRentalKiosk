

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


# this is a base class for student info 
class StudentInfo:

    def __init__(self, student_id,student_status ):

        # attributes or data members 
        self.student_id = student_id
        self.student_status = student_status

        # methods 
        


#Another Base class which will inherate from LaptopRentalInfos so it can get all laptop ID's could be 100+ 
# also student info like if student have a loan or not which will be status 
class RentProcess:
   def __init__(self, student_id, laptop_id,laptop_status,student_status,rental_start_time,due_date):
       
        # Attributes
        self.student_id = student_id
        self.laptop_id = laptop_id 

        #Methods 


