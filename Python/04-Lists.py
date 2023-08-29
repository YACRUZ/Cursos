##Ejercicio 1
print("===== Question 1 =====")
# Complete the function below according to its docstring.
def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None
    return L[1]
print(select_second(L=[1,2,3,4]))


##Ejercicio 2
print("\n===== Question 2 =====")
#You are analyzing sports teams. Members of each team are stored in a list.
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]
print(losing_team_captain(teams=['Paul', 'John', 'Ringo', 'George']))



##Ejercicio 3
print("\n===== Question 3 =====")
#The next iteration of Mario Kart will feature an extra-infuriating new item, the Purple Shell.
def purple_shell(racers):
    #"""Given a list of racers, set the first place racer (at the front of the list) to last
    #place and vice versa.
    
    #>>> r = ["Mario", "Bowser", "Luigi"]
    #>>> purple_shell(r)
    #>>> r
    #["Luigi", "Bowser", "Mario"]
    #"""
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp
    return racers
print(purple_shell(racers=["Mario", "Bowser", "yoshi", "Luigi"]))



##Ejercicio 4
print("\n===== Question 4 =====")
#What are the lengths of the following lists? Fill in the variable lengths with your predictions.
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [len(a), len(b), len(c), len(d)]
print(lengths)




##Ejercicio 5
print("\n===== Question 5 =====")
#We're using lists to record people who attended our party and what order they arrived in
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
print(fashionably_late(arrivals=['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], name='Adela'))