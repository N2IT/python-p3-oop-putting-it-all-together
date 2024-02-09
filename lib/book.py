#!/usr/bin/env python3

class Book:
    
    def __init__(self, title="blank", page_count=10):
        self.title = title
        self.page_count = page_count
        
        # breakpoint()
    
    def turn_page(self):
            print("Flipping the page...wow, you read fast!")

    @property
    def title(self):
        """Getting title of book"""
        return self._title
    

    @title.setter
    def title(self, title):
        self._title = title


    @property
    def page_count(self):
        """retrieve page_count, confirm it is an integer"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print('page_count must be an integer')
  