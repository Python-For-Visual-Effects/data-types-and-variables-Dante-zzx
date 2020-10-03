"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32) 
# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
Number_01 = 64
Number_02 = 32
print(Number_01 + Number_02)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
Name = "Dante"
Age = "24"
Pet = "cat"

print("My name is " + Name + ",my age is " + str(Age) + ",and I love "+ Pet)

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sentece= "This is my first Python program."
Number_01= len(sentece)
print(Number_01)


# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
width= 1920
height= 1080
print("The 10% overscan of 1920 is " +str(width*0.1) + ", and the 1080 is " + str(y*0.1))
