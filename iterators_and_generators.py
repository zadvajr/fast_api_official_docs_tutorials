#Iterators and Generators
#An Iterator is an object that can be iterated over with a loop, they give us one element at time
# An iterator method must implement two methods __iter__() and __next__()
# we can also use iter() and next() in place of __iter__() and __next__()

#An iterator with list
price = [400, 500, 1000, 1200, 1400]

price_iter = price.__iter__()

print(price_iter.__next__()) # 400
print(price_iter.__next__()) # 500
print(price_iter.__next__()) # 1000

#iterating with loop
# when iterating with a loop, if the values are exhausted the iterator 
# raises StopIteration exception all we need to do is to stop StopIteration exception

#Iterating with loop
fruits = ["Apple", "Banana", "Cherry", "Lemon"]
fruits_iter = fruits.__iter__()
while True:
    try:
        print(fruits_iter.__next__())
    except StopIteration:
        break

#Generators - this is an elegant way to create iterators
def return_values():
    yield 1
    yield 2
    yield 3
    yield 'a'
    yield 'b'
    yield 'c'

value = return_values()
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())

#infinite natural numbers
def InfiniteNaturals():
    start = 1
    while start < 100:
        yield start
        start += 1

numbers = InfiniteNaturals()
for item in numbers:
    print(item)