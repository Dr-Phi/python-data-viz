import plotly.express as px

from generate_analyze import *


#Create and roll a D6 and a D10
results, dice = roll_dice(50_000, d6=1, d10=1)

#Analyze results
poss_results, frequencies = analyze_results(results, dice)

#visualize the results
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', "y": 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

# Save HTML
# fig.write_html('./outputs/dice_visual_d6d10.html')
