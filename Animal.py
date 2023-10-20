class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Woof")
cat = Cat("Whiskers")

print(dog.name)  # Output: Rufus
print(cat.name)  # Output: Whiskers

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return True
  else:
    return False

adults = filter(myFunc, ages)
print(adults)
for x in adults:
  print(x)

x = dict(name = "John", age = 36, country = "Norway")

print(x)

#func result mutil values

#use tulpe
def fun(): 
    str = "cafedev.vn"
    x   = 20
    y = 100
    return str, x, y;  # Return tuple, we could also 
                    # write (str, x) 
  
# Driver code to test above method 
str, x, y = fun() # Assign returned tuple 
print(str) 
print(x)
print(y)

#use list
def fun1(): 
    str = "cafedev.vn"
    x = 20   
    y = 100
    return [str, x, 100];   
  
# Driver code to test above method 
list = fun1()  
print(list) 

#use Dictionary
def fun2(): 
    d = dict();  
    d['str'] = "cafedev.vn"
    d['x']   = 20
    d['y']   = 100
    return d 
  
# Driver code to test above method 
d = fun2()  
print(d) 

#lambda func
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(5)

print(mydoubler(2))