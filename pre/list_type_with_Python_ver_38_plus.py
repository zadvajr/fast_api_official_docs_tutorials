#for python version 3.8 and above you have to import List from typing module
from typing import List 
fruits = ["apple", "banana", "cherry", "orange", 23]

def process_items(items: List[str]) -> None:
    for item in items:
        print(item)

process_items(fruits)