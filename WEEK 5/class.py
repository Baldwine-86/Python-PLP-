class Smartphone:
    Brand = "Samsung"
    color = "Gray"
    
    #Method to display Smartphone
    def unlock(self):
        print("The phone is unlocked")
    def lock(self):
        print("The phone is locked")
my_phone = Smartphone()
my_phone.unlock()
my_phone.lock()
print(my_phone.Brand) 

#polymorphism
class Car:
    def move(self):
        return "Driving"
class Plane:
    def move(self):
        return "Flying"
for transport in [Car(), Plane()]:
    print(transport.move())