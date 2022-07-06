import matplotlib.pyplot as plt
from itertools import combinations, permutations

x_inds={0: [0, 4], 1: [4, 8], 2: [8, 12]}
y_inds={0: [0, 4], 1: [4, 8], 2: [8, 12]}

cb=[[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]]
regions=[]

for i in range(6):
    regions+=list(combinations(cb, i))

plt.xlim([0, 12])
plt.ylim([0, 12])

plt.fill_between(x_inds[0], y_inds[1][0], y_inds[1][1], color='k') #1
plt.fill_between(x_inds[1], y_inds[0][0], y_inds[0][1], color='k') #2
plt.fill_between(x_inds[1], y_inds[1][0], y_inds[1][1], color='k') #3
plt.fill_between(x_inds[1], y_inds[2][0], y_inds[2][1], color='k') #4
plt.fill_between(x_inds[2], y_inds[1][0], y_inds[1][1], color='k') #5

plt.fill_between(x_inds[2], y_inds[2][0], y_inds[2][1], color='b')
plt.fill_between(x_inds[2], y_inds[0][0], y_inds[0][1], color='b')
plt.savefig('qr_codes/12345.jpg')

plt.show()