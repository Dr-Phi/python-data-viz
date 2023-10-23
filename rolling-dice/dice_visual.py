import plotly.express as px

from generate_analyze import *

#Create and roll two D6 dice.
results, dice = roll_dice(1000, d6=2)

#Analyze results
poss_results, frequencies = analyze_results(results, dice)

#visualize the results
title = "Results of rolling two D6 Dice 1000 times"
labels = {'x': 'Result', "y": 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)
fig.show()
