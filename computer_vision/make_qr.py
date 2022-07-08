import matplotlib.pyplot as plt

x_inds={0: [0.2, 4.2], 1: [4.2, 8.2], 2: [8.2, 12.2]}
y_inds={0: [0.2, 4.2], 1: [4.2, 8.2], 2: [8.2, 12.2]}

plt.xlim([0, 12])
plt.ylim([0, 12])
plt.figure(figsize=[6,6])

plt.fill_between([0.2, 4.2], 0.2, 4.2, color='k')
plt.fill_between([0.2, 4.2], 8.2, 12.2, color='k')                  #ONLY FOR EMPTY QR CODE
plt.fill_between(x_inds[1], y_inds[1][0], y_inds[1][1], color='k')

#plt.fill_between(x_inds[0], y_inds[1][0], y_inds[1][1], color='k') #1
#plt.fill_between(x_inds[1], y_inds[0][0], y_inds[0][1], color='k') #2
#plt.fill_between(x_inds[1], y_inds[1][0], y_inds[1][1], color='k') #3
#plt.fill_between(x_inds[1], y_inds[2][0], y_inds[2][1], color='k') #4
#plt.fill_between(x_inds[2], y_inds[1][0], y_inds[1][1], color='k') #5

plt.fill_between([0, 0.2], 0, 12.4, color='k') #left
plt.fill_between([12.2, 12.4], 0, 12.4, color='k') #right
plt.fill_between([0, 12.4], 0, 0.2, color='k') #bottom
plt.fill_between([0, 12.4], 12.2, 12.4, color='k') #top

plt.fill_between(x_inds[2], y_inds[2][0], y_inds[2][1], color='m')
plt.fill_between(x_inds[2], y_inds[0][0], y_inds[0][1], color='m')

plt.axis('off')
#plt.savefig('qrcodes/empty.jpg', bbox_inches='tight', pad_inches=0, transparent=True)

#plt.show()