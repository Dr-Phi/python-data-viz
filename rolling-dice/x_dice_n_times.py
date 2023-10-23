import plotly.express as px

from generate_analyze import *


n_times = 10_000

results, dice = roll_dice(n_times, d6=3)

poss_results, frequencies = analyze_results(results, dice)

#visualize the results
title = f"Results of rolling 3 D6 Dice {n_times} times"
labels = {'x': 'Result', "y": 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()
