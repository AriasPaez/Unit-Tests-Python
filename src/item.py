class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def code(self):
        return "{}109".format(self.name)