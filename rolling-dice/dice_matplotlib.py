import matplotlib.pyplot as plt


from generate_analyze import *

#Create and roll two D6 dice.
results, dice = roll_dice(63_000, d6=2)

#Analyze results
categories, frequencies = analyze_results(results, dice)

figsize=(10, 6)
plt.bar(categories, frequencies, color='skyblue')

plt.xlabel('Possible results (sum of dice)')
plt.ylabel('Frequency of result')
plt.title('Results of rolling two D6 Dice 63000 times')

x_positions = range(2, 13)
plt.xticks(x_positions, categories)  # Use custom positions and labels

# Show the graph
plt.show()
# plt.savefig('./outputs/two_d6_pyplot.png')
