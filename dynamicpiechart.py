import matplotlib.pyplot as plt

labels = list(map(str, input("Enter labels values seperated by space: ").split()))
sizes = list(map(float, input("Enter sizes values seperated by space: ").split()))

plt.pie(sizes, labels=labels)
plt.title("DYNAMIC PIE CHART")
plt.show()