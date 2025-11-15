class Students:
    def __init__(self, name):  # 
        self.name = name 
    def __str__(self):
        return f'ሰላም {self.name}'
    def greet(self):
        return f'hello {self.name}'
    

stu_obj = Students('hanna') # create object
print(stu_obj.greet())



class Passengers:
    def __init__(self,name,passport_no ):
        self.name = name
        self.passport_no  = passport_no

    def __str__(self):
        return self.name


class Flight:
    def __init__(self):
        self.destination
        self.departure
        self.passenger = []
        self.capacity 

    def add_passenger(self,name, passport_num):
        obj  = Passengers(name, passport_num)
        if self.capacity <= self.passenger.count():
            return f'the flight is full'
        else:
            self.passenger.append(obj)
            return f'you have sucessfuly booked your flight' 




