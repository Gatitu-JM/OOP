# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class with encapsulation
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.__storage = storage  # Encapsulated (private)
        self.battery = battery

    def install_app(self, app_name):
        return f"Installing {app_name}..."

    def get_storage(self):
        return f"Available storage: {self.__storage} GB"

    def use_storage(self, amount):
        if amount <= self.__storage:
            self.__storage -= amount
            return f"{amount} GB used. Remaining: {self.__storage} GB"
        else:
            return "Not enough storage!"

# Another child class showing polymorphism
class Smartwatch(Device):
    def __init__(self, brand, model, strap_color):
        super().__init__(brand, model)
        self.strap_color = strap_color

    def device_info(self):  # Overriding method (polymorphism)
        return f"{self.brand} {self.model} - Strap Color: {self.strap_color}"


# --- Using the classes ---
phone = Smartphone("Samsung", "Galaxy S25", 128, "4500mAh")
watch = Smartwatch("Apple", "Watch Ultra", "Black")

print(phone.device_info())      # From parent class
print(phone.install_app("WhatsApp"))
print(phone.get_storage())
print(phone.use_storage(10))
print(phone.get_storage())

print("\nSmartwatch Info:")
print(watch.device_info())     
  