from die import Die

def roll_dice(times, **kwargs):
    """roll_dice(50, d4=1, d6=2)
    will create 3 dice: 1 of 4 sides and 2 of 6 sides
    and will roll them 50 times, returning a list with 50 numbers (sum of dice for each time)
    you can decide the number of SIDES (#) of your dice by using d#=ammount
    """

    dice = {}
    i = 1
    for die_type, value in kwargs.items():
        for _ in range(value):
            key_name = f"die{i}"
            sides = int(die_type[1:])
            dice[key_name] = Die(sides)
            i += 1

    results = []
    for _ in range(times):
        #list comprehension and sum() to calculate the sum of the dice when rolling them
        result = sum(die.roll() for die in dice.values())
        results.append(result)

    return (results, dice)



# Analyze results
def analyze_results(results, dice):
    """(list, dict)
    receives a list with X results from rolling dice (dict)
    and returns the frequencies each possible number (result) got."""
    frequencies = []
    i=0
    max_result = 0
    for die in dice.values():
        max_result += die.num_sides
        i += 1
    print(f"Range of possible results: {i} - {max_result}")

    poss_results = range(i, max_result+1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    return frequencies

# # Test functions
# print(roll_dice(5, d4=1, d6=2))
# res, di = roll_dice(100, d4=1, d6=2)
# print(analyze_results(res, di))
