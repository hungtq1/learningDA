#Converts the first character to upper case

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


txt = "36 is my age."

x1 = txt.capitalize()

print (x1)


#Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"
x = txt.center(20)
print(x)


#Using the letter "O" as the padding character:
txt = "banana"
x = txt.center(20, "O")
print(x)

#Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

#UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x)


#These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

#endswith()	Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

#Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

#Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.find("l", 5, 10)
print(x)
print(txt.find("q"))

#format() Method
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

#index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q"))
#print(txt.index("q"))

#Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x) #true

txt = "Company 12"
x = txt.isalnum()
print(x) #false

#Check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x) #true

txt = "Company10"
x = txt.isalpha()
print(x)

#Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

#split
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 2)
print(x)

#Make the first letter in each word upper case:
txt = "Welcome to my world"
x = txt.title()
print(x)

#Note that the first letter after a non-alphabet letter is converted into a upper case letter:
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)


#Upper case the string:
txt = "Hello my friends"
x = txt.upper()
print(x)


#Check if the string starts with "Hello":
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)


#Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su aba."
x = txt.rindex("casa")
print(x)

#
txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)