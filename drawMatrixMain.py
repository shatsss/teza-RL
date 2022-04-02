import matplotlib.pyplot as plt

# grid = np.random.rand(4, 4)
# data = [[135, 120], [62, 110]]
# x = ['6_1', '6_2']
# y = ['alone', 'opponent']
# plt.title('6 alone')
# # plt.xlabel('alone')
# # plt.ylabel('opponent')
# plt.imshow(data, interpolation='none')
# plt.xticks(range(len(x)), x, fontsize=12)
# plt.yticks(range(len(y)), y, fontsize=12)
# for i in range(2):
#     for j in range(2):
#         c = data[j][i]
#         plt.text(i, j, str(c), va='center', ha='center')
# plt.colorbar()
# plt.legend()
# plt.show()


# coverage
data = [[14.5, 13], [21, 20], [19, 21.5], [0, 21]]
x = ['6_1', '6_2']
y = ['alone', 'opponent', 'same-pheromones', 'deleting pheromones']
plt.title('6 opponent coverage')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(4):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()

# number of wins
data = [[0.59, 0.708], [0.527, 0.648], [0, 0.752]]
x = ['6_1', '6_2']
y = ['opponent', 'same-pheromones', 'deleting pheromones']
plt.title('6 opponent wins')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(3):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()
# size 2 deleting pheromones
# Number of wins: 0.752
# Number of loses: 0.169
# Number of draws: 0.079
# grid size 2 same pheromones
# Number of wins: 0.648
# Number of loses: 0.274
# Number of draws: 0.078
# grid size 1 same pheromones
# Number of wins: 0.527
# Number of loses: 0.403
# Number of draws: 0.07
# grid size 2 opponent
# Number of wins: 0.708
# Number of loses: 0.214
# Number of draws: 0.078
# grid size 1 opponent
# Number of wins: 0.59
# Number of loses: 0.335
# Number of draws: 0.075


# data = [[480, 465], [430, 345]]
# x = ['10_1', '10_2']
# y = ['alone', 'opponent']
# plt.title('10 alone')
# # plt.xlabel('alone')
# # plt.ylabel('opponent')
# plt.imshow(data, interpolation='none')
# plt.xticks(range(len(x)), x, fontsize=12)
# plt.yticks(range(len(y)), y, fontsize=12)
# for i in range(2):
#     for j in range(2):
#         c = data[j][i]
#         plt.text(i, j, str(c), va='center', ha='center')
# plt.colorbar()
# plt.legend()
# plt.show()

data = [[41, 44], [45.5, 56.5], [48, 55.5], [0, 0]]
x = ['10_1', '10_2']
y = ['alone', 'opponent', 'same pheromones', 'deleting pheromones']
plt.title('10 opponent coverage')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(4):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()

# number of wins
data = [[0.492, 0.695], [0.436, 0.705], [0, 0]]
x = ['10_1', '10_2']
y = ['opponent', 'same-pheromones', 'deleting pheromones']
plt.title('10 opponent wins')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(3):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()
# grid size 1  with same pheromones
# Number of wins: 0.436
# Number of loses: 0.53
# Number of draws: 0.034
# grid size 2  with same pheromones
# Number of wins: 0.705
# Number of loses: 0.274
# Number of draws: 0.021
# grid size 2
# Number of wins: 0.695
# Number of loses: 0.289
# Number of draws: 0.016
# grid size 1
# Number of wins: 0.492
# Number of loses: 0.487
# Number of draws: 0.021


data = [[75, 72], [81.5, 75], [0, 0]]
x = ['14_1', '14_2']
y = ['opponent', 'same pheromones', 'deleting pheromones']
plt.title('14 opponent coverage')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(3):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()



# number of wins
data = [[0.121, 0.041], [0.258, 0.223], [0, 0]]
x = ['14_1', '14_2']
y = ['opponent', 'same-pheromones', 'deleting pheromones']
plt.title('14 opponent wins')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(3):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()

# grid size 14

# grid size 1 opponent
# Number of wins: 0.121
# Number of loses: 0.871
# Number of draws: 0.008

# grid size 1 same pheromones
# Number of wins: 0.258
# Number of loses: 0.724
# Number of draws: 0.018


# grid size 2 same pheromones
# Number of wins: 0.223
# Number of loses: 0.76
# Number of draws: 0.017

# grid size 2
# Number of wins: 0.041
# Number of loses: 0.954
# Number of draws: 0.005
