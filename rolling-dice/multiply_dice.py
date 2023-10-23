import plotly.express as px

from die import Die

die1 = Die()
die2 = Die()

results = [die1.roll() * die2.roll() for _ in range(1000)]

# Analyze the results
poss_results = range(1, (die1.num_sides ** 2) + 1)
frequencies = [results.count(value) for value in poss_results]


# visualize the results
title = "Results from products of rolling 2 D6 Dice 1000 times"
labels = {'x': 'Result', "y": 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()
