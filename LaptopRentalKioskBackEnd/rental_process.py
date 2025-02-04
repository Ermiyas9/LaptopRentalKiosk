
#Another Base class which will inherate from LaptopRentalInfos so it can get all laptop ID's could be 100+ 
# also student info like if student have a loan or not which will be status 
class RentProcess:
   def __init__(self, student_id, laptop_id,laptop_status,student_status,rental_start_time,due_date):
       
        # Attributes
        self.student_id = student_id
        self.laptop_id = laptop_id 

        #Methods 