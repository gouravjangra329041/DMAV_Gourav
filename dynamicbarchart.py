import matplotlib.pyplot as plt

x=list(map(str, input("Enter X values seperated by space: ").split()))
y=list(map(float, input("Enter Y values seperated by space: ").split()))

plt.bar(x,y)
plt.title("DYNAMIC BAR CHART")
plt.bar(x,y,color='blue')
plt.show()