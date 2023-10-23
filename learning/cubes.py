import matplotlib.pyplot as plt

x_values = range(1, 100)
y_values = [x ** 3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')

plt.show()
# plt.savefig('./outputs/cubes_plot.png', bbox_inches='tight')
