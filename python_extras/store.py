class Product:
    def __init__(self, name, price, category,):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        self.is_increased = is_increased
        self.percent_change = percent_change
        if self.is_increased == True:
            self.price *= self.percent_change
        else:
            self.price /= self.percent_change
        return self

    def print_info(self):
        print(f"Name of product: {self.name}\nCategory: {self.category}\nPrice: {self.price}")

class Store:
    def __init__(self, name, product):
        self.name = name
        self.product_list = []
        self.new_product = product

    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self

    def sell_product(self, id):
        self.product_list.pop(id)
        return self

    def store_info(self):
        print(f"Store name: {self.name}\nStore products: {self.product_list}")

    def inflation(self, percent_increase, price):
        pass

    def set_clearence(self, category, percent_discount):
        pass


computer = Product("Computer", 800.00, "Laptops & Computers")
monitor = Product("Monitor", 550.00, "TV,s & Monitors")
keyboard = Product("Keyboard", 100.00, "Peripherals")

computex = Store("Computex", computer)
computex.add_product(monitor).add_product(keyboard).store_info()

monitor.update_price(0.75, True).print_info()
