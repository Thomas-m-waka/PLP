# Object-Oriented Programming Assignment 🏗️
# This program demonstrates classes, inheritance, and polymorphism in Python.

# -----------------------------
# Step 1: Define a Parent Class (Smartphone)
# -----------------------------

class Smartphone:
    """A class representing a generic smartphone."""

    def __init__(self, brand, model, storage, battery):
        """Initialize smartphone attributes."""
        self.brand = brand
        self.model = model
        self.storage = storage  # Storage in GB
        self.battery = battery  # Battery capacity in mAh

    def get_info(self):
        """Return basic information about the smartphone."""
        return f"{self.brand} {self.model}: {self.storage}GB, {self.battery}mAh battery"

    def charge(self):
        """Simulate charging the phone."""
        return f"{self.model} is charging... 🔋"

# -----------------------------
# Step 2: Create Child Classes (iPhone & Samsung)
# -----------------------------

class iPhone(Smartphone):
    """A class representing an iPhone, inheriting from Smartphone."""

    def __init__(self, model, storage, battery, face_id):
        """Initialize an iPhone with Face ID feature."""
        super().__init__("Apple", model, storage, battery)
        self.face_id = face_id  # Boolean (True/False)

    def unlock(self):
        """Simulate unlocking the iPhone using Face ID."""
        return f"{self.model} unlocked using Face ID! 😊"

class Samsung(Smartphone):
    """A class representing a Samsung phone, inheriting from Smartphone."""

    def __init__(self, model, storage, battery, stylus):
        """Initialize a Samsung phone with a stylus."""
        super().__init__("Samsung", model, storage, battery)
        self.stylus = stylus  # Boolean (True/False)

    def use_stylus(self):
        """Simulate using a stylus on a Samsung device."""
        return f"Using the stylus on {self.model} ✍️"

# -----------------------------
# Step 3: Implement Polymorphism (Move Method)
# -----------------------------

class MovingObject:
    """A parent class for moving objects (Animals, Vehicles, etc.)."""

    def move(self):
        """Common move method (to be overridden in child classes)."""
        pass

# Animal subclasses with different move behaviors
class Bird(MovingObject):
    def move(self):
        return "Flying in the sky! 🦅"

class Fish(MovingObject):
    def move(self):
        return "Swimming in the water! 🐠"

# Vehicle subclasses with different move behaviors
class Car(MovingObject):
    def move(self):
        return "Driving on the road! 🚗"

class Plane(MovingObject):
    def move(self):
        return "Flying through the clouds! ✈️"

# -----------------------------
# Step 4: Testing the Classes
# -----------------------------

if __name__ == "__main__":
    # Creating instances of Smartphones
    iphone = iPhone("iPhone 15 Pro", 256, 4300, True)
    samsung = Samsung("Galaxy S23 Ultra", 512, 5000, True)

    # Printing smartphone details
    print(iphone.get_info())   # Apple iPhone 15 Pro: 256GB, 4300mAh battery
    print(iphone.unlock())     # iPhone 15 Pro unlocked using Face ID!

    print(samsung.get_info())  # Samsung Galaxy S23 Ultra: 512GB, 5000mAh battery
    print(samsung.use_stylus()) # Using the stylus on Galaxy S23 Ultra ✍️

    # Testing Polymorphism
    objects = [Bird(), Fish(), Car(), Plane()]

    # Calling the move() method on different objects
    for obj in objects:
        print(obj.move())

    # Output:
    # Flying in the sky! 🦅
    # Swimming in the water! 🐠
    # Driving on the road! 🚗
    # Flying through the clouds! ✈️
