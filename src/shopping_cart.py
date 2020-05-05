class NotExistsItemError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def clear_items(self):
        self.items.clear()
    
    def get_item(self, item):
        if item not in self.items:
            raise NotExistsItemError('Item does not exists')
        else:
            return self.items[self.items.index(item) - 1]
    
    def contains_items(self):
        return len(self.items) > 0

    def total(self):
        return sum([item.price for item in self.items])