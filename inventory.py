# inventory.py
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return list(self.items)
