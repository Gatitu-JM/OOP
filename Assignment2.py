# Parent class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Child classes with different move() implementations
class Car(Vehicle):
    def move(self):
        print("Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the sea!")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling along the path!")

# --- Using polymorphism ---
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()
