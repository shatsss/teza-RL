import matplotlib.pyplot as plt

x = [5, 7, 10, 15]
y = [ [230,290,430 ,810], [920,280,400,4000 ], [720,700,600,4000] ,[400,320,800,4000], [233.74,522.95,1457.61,4082.99]]
labels = ['5on5', '7on7', '10on', '15on15', 'random']

for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)

plt.legend()
plt.show()