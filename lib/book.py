#!/usr/bin/env python3

class Book:
    
    def __init__(self, title="blank", page_count=10):
        self.title = title
        self.page_count = page_count
        # breakpoint()


    def get_title(self):
        """Getting title of book"""
        return self._title
    
   
    def set_title(self, title):
        self._title = title

    title = property(get_title, set_title)



    def get_page_count(self):
        """retrieve page_count, confirm it is an integer"""
        return self._page_count
    

    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print('page_count must be an integer')
            

    page_count = property(get_page_count, set_page_count)
    
book = Book("hey its a book", 200)