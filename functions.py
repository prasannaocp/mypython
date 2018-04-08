# learning functions - DRY - Dont Repeat yourself . Write once , Use Many
#def function_name():
    #Code Block
#function to be defined first before calling

def your_age(age):
    print ('your age is :{}' .format(age))
#yourage() TypeError: yourage() missing 1 required positional argument: 'age'
your_age(33)
print (type(your_age))
#print (type(age))

def name_age(name='John Cena' , age=26):
    """This is my doc string - Doc sring provides summary of function - This function is used to get name age and prints it.
help(function_name) get the information about function"""
    print (' Welcome to Programming World of Python!! - Hey {}  your age is {} !!!' .format (name,age))
name_age()
name_age('Braun',33)
name_age(33)
name_age(age=21)   
name_age(name='Roman Reigns')
name_age(age=40,name="Kane")
x=input ("Enter your name:")
y=input ("Enter your age:")
y=int(y)
name_age(x,y)
help (name_age)



