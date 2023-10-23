import plotly.express as px
import pandas as pd

from random_walk import RandomWalk

#Make a random walk
rw = RandomWalk()
rw.fill_walk()

X = rw.x_values

Y = rw.y_values

df = pd.DataFrame({'X': X, 'Y': Y})

# Create a scatter plot
fig = px.scatter(df, x='X', y='Y', title='Random Walk with 5000 points')

# Highlight the initial (green) and last (red) point
fig.add_scatter(x=[X[0]], y=[Y[0]], mode='markers', marker=dict(size=15, color='green'), name='Start')
fig.add_scatter(x=[X[-1]], y=[Y[-1]], mode='markers', marker=dict(size=15, color='red'), name='Finish')

# Save the plot
fig.write_html('./outputs/random_walk_plotly.html')
