##Ejercicio 1
print("===== Question 1 =====")
#Have you ever felt debugging involved a bit of luck? The following program has a bug.
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False
print(has_lucky_number([5,7,5,3]))



##Ejercicio 2
print("\n===== Question 2 =====")
# Implement a function that reproduces this behaviour, returning a list of booleans corresponding to whether the corresponding element is greater than n
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    res=[]
    for lt in L:
        if lt>thresh:
            res.append(True)
        else:
            res.append(False)
        
    return res
print(elementwise_greater_than([1,2,3,4,5],2))



##Ejercicio 3
print("\n===== Question 3 =====")
#Complete the body of the function below according to its docstring.
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
print(menu_is_boring(["bistec", "eggs", "pozole", "pozole"]))



##Ejercicio 4
print("\n===== Question 4 =====")
#Complete the following function to calculate the average value per play of the slot machine.
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    avg_payout = sum(payouts) / n_runs
    return avg_payout
print(estimate_average_slot_payout(100))