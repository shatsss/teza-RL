import matplotlib.pyplot as plt

x = [5, 7, 10,15]
y = [[72.38, 220, 850,1100], [60.0, 130, 820,1100], [100, 550, 450,2000], [417.75, 430,2000,2000 ],
     [233.74, 522.95, 1365,2000]]
labels = ['5_1', '7_1', '10_1', '15_1', 'random']

for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)
plt.legend()
plt.show()
x = [5, 7, 10]
y = [[400, 1800, 2000 ], [60, 2000, 1000 ], [50, 700, 2000 ], [2000, 2000, 2000 ],
     [233.74, 522.95, 1365 ]]
labels = ['5_2', '7_2', '10_2', '15_2', 'random']

for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)
plt.legend()
plt.show()
x = [5, 7, 10]
y = [[70, 2000, 2000], [75, 800, 2000], [420, 2000, 2000], [2000, 2000, 2000],
     [233.74, 522.95, 1365]]
labels = ['5_3', '7_3', '10_3', '15_3', 'random']

for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)

plt.legend()
plt.show()
