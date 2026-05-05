class Eagle:


    species = "bird"


    def __init___(self, name, age): # constructor function
        self.name = name
        self.age = age





Eagleobject1 = Eagle('Beaky', 10)
Eagleobject2 = Eagle('blue', 13)

print("{} is {} years old" .format(Eagleobject1.name, Eagleobject1.age))
print("'Beaky' is a {} " .format(Eagleobject1.species))