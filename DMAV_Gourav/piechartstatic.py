import matplotlib.pyplot as plt

labels = 'Apple', 'Orange', 'Banana', 'DragonFruit'
sizes = [15, 30, 40, 65]

plt.pie(sizes, labels=labels)
plt.title("STATIC PIE CHART")
plt.show()