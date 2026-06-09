#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 1
    @property
    def page_count(self):
        return self._page_count
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
    
    def turn_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print("Flipping the page...wow, you read fast!")

if __name__ ==" __main__":
    title_input = input("Please enter the title")
    count_input = input("Please enter the page count")

    my_book  = Book(title_input, count_input)
    my_book.turn_page()

        