#Python Type Introduction
#Python has support for optional type hints also called type annotation
#these type hints or annotations are special syntax that allow defining a type of variable
#by declaring types for your variables editors and tools can give you better support.
#fastapi is based on all these type hints - they give it many advantage or benefits
#Simple Example
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("daniel", "zadva")) #outputs: Daniel Zadva
#the point is type hints helps with autocompletion

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old " + str(age)
    return name_with_age

print(get_name_with_age("Daniel", 33))

