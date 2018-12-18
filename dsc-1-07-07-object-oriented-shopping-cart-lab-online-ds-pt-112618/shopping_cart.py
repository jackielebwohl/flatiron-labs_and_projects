class ShoppingCart:
    def __init__(self, total=0, items =[], employee_discount=0):
        self._total=total
        self._items=items
        self._employee_discount=employee_discount 
    def total (self):
        return self._total
    def items (self):
        return self._items
    def employee_discount(self):
        return self._employee_discount
    
    def add_item(self, item, price, quantity=1):
        item_dict={'item': item, 'price': price, 'quantity': quantity}
        self._items.append(item_dict)
        self._total += price * quantity
        return self._total
   
    def mean_item_price(self):
        num_items=[]
        for item in self._items:
            num_items.append(item['quantity'])
        return self._total / sum(num_items)
 #   def median_item_price(self):
  #      list_of_prices=[]
   #     for item in self._items:
    #        if item['quantity'] == 1:
     #           list_of_prices.append(item['price'])
      #      else:
       #         list_of_prices.append([item['price']] * item['quantity'])    
        #return list_of_prices
        #prices_sorted=float(list_of_prices).sort()
        #if len(list_of_prices) %2 == 0:
         #   index_1= int(len(list_of_prices))/2 - 1
          #  index_2= int(len(list_of_prices))/2 
           # median= (prices_sorted[index_1] + prices_sorted[index_2]) / 2
            #return median
       # else:
        #    index_number= (len(list_of_prices)-1) / 2
         #   return prices_sorted[index_number]
           
    def apply_discount(self):
        if self._employee_discount:
            multiplier = (100-self._employee_discount)/100
            return self._total * multiplier
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
        return list_of_items
    def void_last_item(self):
        if self._items:
            removed_item=self._items.pop()
            self._total -= removed_item['price']
        else: 
            return "There are no items in your cart!"
        