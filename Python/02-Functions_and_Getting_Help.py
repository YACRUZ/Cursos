##Ejercicio 1
print("===== Question 1 =====")
def round_to_two_places(num):
    #"""Return the given number rounded to two decimal places. 
    
    #>>> round_to_two_places(3.14159)
    #3.14
    #"""
    # Replace this body witqh your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return round(num,2)
print(round_to_two_places(3.14159))

##Ejercicio 2
print("\n===== Question 2 =====")
# Put your test code here
print(round(10145.191,-2))

##Ejercicio 3
print("\n===== Question 3 =====")
def to_smash(total_candies, n_friends):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n_friends
print(to_smash(91, 3))
