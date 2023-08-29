
##Ejercicio 1
print("===== Question 1 =====")
#Add the title "Results of 500 slot machine pulls", Make the y-axis start at 0., Add the label "Balance" to the y-axis
def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    # Complete steps 2 and 3 here
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")


graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph


##Ejercicio 2
print("\n===== Question 2 =====")
#Luigi is trying to perform an analysis to determine the best items for winning races on the Mario Kart circuit. 
def best_items(racers):
    winner_item_counts = {}
    for rango in range(len(racers)):
        racer = racers[rango]
        if racer['finish'] == 1:
            for item in racer['items']:
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1

        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                rango+1, len(racers), racer['name'])
                 )
    return winner_item_counts

sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
print(best_items(sample))



##Ejercicio 3
print("\n===== Question 3 =====")
#Fill in the body of the blackjack_hand_greater_than function according to the docstring.
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    def get_num(string):
        if string in ('J', 'Q', 'K'):
            return 10
        if string == 'A':
            return 11
        return int(string)
    
    def get_hand_num(hand):
        list_num = [get_num(x) for x in hand]
        num_aces = len([x for x in list_num if x >= 11])
        total_sum = sum([x for x in list_num if x < 11])
        total_sum = total_sum + num_aces
        while total_sum + 10 <= 21 and num_aces > 0:
            total_sum += 10
            num_aces -= 1
        return total_sum
    
    suma_hand_1 = get_hand_num(hand_1)
    suma_hand_2 = get_hand_num(hand_2)
    return suma_hand_1 <= 21 and (suma_hand_1 > suma_hand_2 or suma_hand_2 > 21)       


print(blackjack_hand_greater_than(['K'], ['3', '4']))
print(blackjack_hand_greater_than(['K'], ['10']))
print(blackjack_hand_greater_than(['K', 'K', '2'], ['3']))