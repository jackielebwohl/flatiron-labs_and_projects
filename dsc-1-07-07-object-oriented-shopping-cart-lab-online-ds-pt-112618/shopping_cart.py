import numpy as np
class ShoppingCart:
    def __init__(self, total=0, items =[], employee_discount=0):
        self._total=total
        self._items=items
        self._employee_discount=employee_discount 
    
    #total
    def get_total (self):
        return f" Your total is ${self._total}."
    def set_total (self, new_total):
        self._total = self._total + new_total
        return f" You have spent ${self._total} total." 
        
    total=property(get_total, set_total)
        
    
    #items
    def get_items (self):
        return f" Your cart contains: {self._items}."
    def set_items(self, list_of_items):
        self._items = self._items.append(list_of_items)
        return f"Your cart contains: {self._items}"
    items=property(get_items, set_items)
    
    #employee discount
    def get_employee_discount(self):
        return f" Your employee discount is {self._employee_discount}% off."
    def set_employee_discount(self, discount=0):
        self._employee_discount=discount
        return f" You're next order will receive {self._employee_discount}% off."
    employee_discount=property(get_employee_discount, set_employee_discount)
    
    def add_item(self, item, price, quantity=1):
        item_dict={'item': item, 'price': price, 'quantity': quantity}
        self._items.append(item_dict)
        self._total += price * quantity
        return f" You are purchasing {self._items} for ${self._total}"
   
    def mean_item_price(self):
        num_items=[]
        for item in self._items:
            num_items.append(item['quantity'])
        mean = self._total / sum(num_items)
        return f"Your average item costs ${mean}."
    
    def median_item_price(self):
        list_of_prices=[]
        for item in self._items:
            iteration_count = item['quantity']
            while iteration_count >0:
                list_of_prices.append(item['price'])
                iteration_count -= 1
            else: 
                continue
        median = np.median(list_of_prices)
        return f"Your median item price is {median}."
           
    def apply_discount(self):
        if self._employee_discount:
            multiplier = (100-self._employee_discount)/100
            discounted_total = self._total * multiplier
            return f" Your discounted total at {self._employee_discount}% off is ${discounted_total}."
        else:
            return "Sorry, there is no discount to apply to your cart :("
    
    def item_names (self):
        list_of_items=[]
        for item in self._items:
            iteration_count = item['quantity']
            while iteration_count >0:
                list_of_items.append(item['item'])
                iteration_count -= 1
            else:
                continue
        return f" You are purchasing {list_of_items}."
   
    def void_last_item(self):
        if self._items:
            removed_item=self._items.pop()
            self._total -= removed_item['price']
        else: 
            return "There are no items in your cart!"
        