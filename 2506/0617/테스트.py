class Parent:
    x = 10

class Child(Parent):
    x = 15

p = Child()
print(p.x)