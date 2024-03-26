print("hotpotato")

#variables 
#red_bucket = input("what is in the bucket" )
print(red_bucket) 

del red_bucket #this deletes the variable pervious to the line

age = 100 
print(age)
print(type(age))

#operators (==, !=, >, <, >=, <=)
print(5!=4)
print(5==4)
print(5>4)
print(5<4)

#if, eli f& else, statements
thomas_age=10
age_at_kindergarten=5
if thomas_age < age_at_kindergarten:
    print("he should be in pre-school")
elif thomas_age == age_at_kindergarten:
    print("enjoy kindergarten")
else:
    print("he should be in another class")

#functions into which you inset values
def school_age_calculator(age,name):
    if age < 5:
        print("enjoy the time!", name, "is only", age)
    elif age == 5:
        print("enjoy kindergarden", name)
    else:
        print("they grow up so fast")

school_age_calculator(3,"thomas")

#functions from which you get a value back
def add_ten_to_age(age):
    new_age = age + 10
    return new_age

how_old_will_i_be = add_ten_to_age(3)
print(how_old_will_i_be)

#functions
def print_comment():   # definition of function
    text = "we can do this!!"
    print(text)
    print(text)
    print(text)
print_comment()

def print_comm(text): #insert value into function
    print(text)
    print(text)
print_comm("one more time")

#loops that executes code mutiple times
#while loop
x=0 #where x is 0
while (x<5): #and x is less than 5
    print(x) #print all the values that are less
    x=x+1 #becausse it will start at 0 and you want all the values thereafter you add 1

#for loop
for x in range(5,10): #starts from 5 and ends at 10(not including 10)
    print(x)

#variables of different days
days=["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

for d in days: #creating d as a variable for days
    if(d=="thu"):break #when days reach thu it stops, if you use continue instead of break it jumps over thu
    print(d) #prints d as instructed above

#libraries - existing data that can be used
import math #math is an in-built library
print("pi is", math.pi) #math.pi uses tha value of pi and it displays this from the library


#stack overflow, chatgpt and blackbox.ai helps with errors 
