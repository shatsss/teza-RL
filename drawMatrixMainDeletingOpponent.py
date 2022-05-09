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


data = [[0, 21], [0, 18]]
x = ['6_1', '6_2']
y = ['deleting pheromones', 'new-grade-function']
plt.title('6 opponent coverage')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(2):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()

# number of wins
data = [[0, 0.752], [0, 0.508]]
x = ['6_1', '6_2']
y = ['deleting pheromones', 'new-grade-function']
plt.title('6 opponent wins')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(2):
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
# far from opponent
# Number of wins: 0.858
# Number of loses: 0.104
# Number of draws: 0.038


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

data = [[0, 59], [0, 56]]
x = ['10_1', '10_2']
y = ['deleting pheromones', 'new-grade-function']
plt.title('10 opponent coverage')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(2):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()

# number of wins
data = [[0, 0.909], [0, 0.774]]
x = ['10_1', '10_2']
y = ['deleting pheromones', 'new-grade-function']
plt.title('10 opponent wins')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(2):
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
# 10 2 deleting pheromones
# Number of wins: 0.909
# Number of loses: 0.074
# Number of draws: 0.017
# close to opponent
# Number of wins: 0.84
# Number of loses: 0.142
# Number of draws: 0.018
# new function grade
# Number of wins: 0.774
# Number of loses: 0.206
# Number of draws: 0.02
data = [[0, 100], [0, 97], [0, 98], [0, 92], [0, 92]]
x = ['14_1', '14_2']
y = ['deleting pheromones', '6 deleting pheromones', '10 deleting pheromones',
     'new-grade-function-6',
     'new-grade-function-10']
plt.title('14 opponent coverage')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(5):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()

# number of wins
data = [[0, 0.578], [0, 0.503], [0, 0.623], [0, 0.394], [0, 0.6]]
x = ['14_1', '14_2']
y = ['deleting pheromones', '6 deleting pheromones', '10 deleting pheromones',
     'new-grade-function-6',
     'new-grade-function-10']
plt.title('14 opponent wins')
# plt.xlabel('alone')
# plt.ylabel('opponent')
plt.imshow(data, interpolation='none')
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
for i in range(2):
    for j in range(5):
        c = data[j][i]
        plt.text(i, j, str(c), va='center', ha='center')
plt.colorbar()
plt.legend()
plt.show()

# grid size 14
# 6_2_deleting_pheromones_grade_according_to_grid_size
# Number of wins: 0.394
# Number of loses: 0.588
# Number of draws: 0.018
# 6_2_close_to_opponent
# Number of wins: 0.15
# Number of loses: 0.822
# Number of draws: 0.028
# 6_2_far_to_opponent
# Number of wins: 0.072
# Number of loses: 0.92
# Number of draws: 0.008
# 10_2_far_to_opponent
# Number of wins: 0.136
# Number of loses: 0.858
# Number of draws: 0.006
# 10_2_deleting_pheromones_grade_according_to_grid_size
# Number of wins: 0.6
# Number of loses: 0.378
# Number of draws: 0.022
# 10_2_close_to_opponent
# Number of wins: 0.352
# Number of loses: 0.628
# Number of draws: 0.02
# grid size 2 with deleting pheromones size 10
# Number of wins: 0.623
# Number of loses: 0.36
# Number of draws: 0.017


# deleting pheromones size 6
# Number of wins: 0.503
# Number of loses: 0.486
# Number of draws: 0.011


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

# grid size 2 with deleting pheromones
# Number of wins: 0.578
# Number of loses: 0.395
# Number of draws: 0.027


data = [[0, 160], [0, 160], [0, 160]]
x = ['20_1', '20_2']
y = ['6_deleting_pheromones', '10_deleting_pheromones', '14_deleting_pheromones']
plt.title('20 opponent coverage')
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
data = [[0, 0.055], [0, 0.168], [0, 0.132]]
x = ['20_1', '20_2']
y = ['6_deleting_pheromones', '10_deleting_pheromones', '14_deleting_pheromones']
plt.title('20 opponent wins')
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
######### 20
# 14_2_deleting_pheromones
# Number of wins: 0.132
# Number of loses: 0.862
# Number of draws: 0.006

# 10_2_deleting_pheromones
# Number of wins: 0.168
# Number of loses: 0.822
# Number of draws: 0.01

# 6_2_deleting_pheromones
# Number of wins: 0.055
# Number of loses: 0.941
# Number of draws: 0.004
