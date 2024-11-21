#for python version 3.9 and above 
fruits = ["apple", "banana", "cherry", "orange"]

def process_items(items: list[str]) -> None:
    for item in items:
        print(item.upper())

process_items(fruits)