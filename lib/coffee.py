#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value
    def tip(self):
        self.price +=1
        print("This coffee is great, here’s a tip!")
if __name__ == "__main__":
    size_input = input("PLease enter the size")
    price_input = input("PLease enter the size")

    my_coffee = Coffee(size_input, price_input)
    my_coffee.tip()