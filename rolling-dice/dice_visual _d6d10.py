import plotly.express as px

from die import Die

#CReate a D6 and a D10

die1 = Die()
die2 = Die(10)

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#Analyze results
frequencies = []
max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
