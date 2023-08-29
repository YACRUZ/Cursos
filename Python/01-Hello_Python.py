##Ejercicio 0
print("===== Question 0 =====")
# create a variable called color with an appropriate value on the line below
# (Remember, strings in Python must be enclosed in 'single' or "double" quotes)
color="blue"
print("Favorite color: " + color)


##Ejercicio 1
print("\n===== Question 1 =====")
pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius= diameter/2
print("Radius: " + str(radius))

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area=(pi*(radius*radius))
print("Area: " + str(area))


##Ejercicio 2
print("\n===== Question 2 =====")
########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]

print("a (inicial): " + str(a) + ", b (inicial): " + str(b))
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.
tmp=a
a=b
b=tmp

print("a (final): " + str(a) + ", b (final): " + str(b))


##Ejercicio 3a
print("\n===== Question 3a =====")
#Add parentheses to the following expression so that it evaluates to 1.
5 - 3 // 2
#Solution
print("Solution: " + "((5 - 3) // 2) = " + str(((5 - 3) // 2)))


##Ejercicio 3b
print("\n===== Question 3b =====")
#Add parentheses to the following expression so that it evaluates to 0.
8 - 3 * 2 - 1 + 1
#Solution
print("Solution: " + "((8 - 3) * (2 - (1 + 1))) = " + str(((8 - 3) * (2 - (1 + 1)))))



##Ejercicio 4
print("\n===== Question 4 =====")
# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash=(alice_candies + bob_candies + carol_candies)%3
print("To smash: " + "(alice_candies + bob_candies + carol_candies)%3 = " + str(to_smash))
