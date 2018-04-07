#age=(input()) # TypeError: '>=' not supported between instances of 'str' and 'int'.
age = input ("Please enter your age: ")
print (type(age))
print ("By default input is consdered as string, so convert into Int")
age=int(age)
print (type(age))
print ("Your age is. ", age)
if age<20:
    print ("Love your books")
elif age >=20 and age < 40: # if,else - conditional statement ends with : 
    print ("love your life and live every moment of it")
elif age>=40 and age <120: # mulltiple elif statement allowed on python
    print ('life begins @ 40, So enjoy your life')
else:
    print ('tell your right age - is that a DEAD MAN living')
print ("Dont read this crazy code !! - I am new to python")    # not in code block, gets printed every time
