myArray = []
animals = ["cat", "dog", "bird"]
number = [1, 2, 3, 4, 5]

print(animals[0])
print(animals[-1])
print(len.animals)

element1 = animals[0]

animals.append("sheep")
print(animals)
animals.insert(0, "cow")
print(animals)

animals[1] = "puppy"
print(animals)

animals.pop() removes last element by default
print(animals)

animals.pop(0)
print(animals)

del animals[1]
print(animals)

animals.remove("dog")
print(animals)

number = [5, 3, 7, 9, 2,]
print(sort(number)) temporary sort
number.sort() permenant sort
number.sort(reverse=True) actual reverse
number.sort(reverse) 

for n in numbers:
    print(n)

for animal in animals:
    print(animal)

for index in range(0, 100):    if you dont define a starting position, it assumes 0
    print(index)

for i in range(0, len(number)):  prints only list of numbers
    print(number[i])