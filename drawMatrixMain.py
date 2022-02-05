import matplotlib.pyplot as plt

x = [5, 7, 10, 15]
y = [ [50,250,700,0 ], [50,130,500,0 ], [70,200,0,0] ,[0,0,0,0]]
labels = ['5on5', '7on7', '10on', '15on15']

for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)

plt.legend()
plt.show()