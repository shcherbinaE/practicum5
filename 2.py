import matplotlib.pyplot as plt

xc = int(input('xc = '))
yc = int(input('yc = '))
r = int(input('r = '))
x = int(input('x = '))
y = int(input('y = '))

figure, axes = plt.subplots()
circle1 = plt.Circle((xc, yc), r, color='r')
plt.plot(x, y, color='green', marker='o', markersize=7)

axes.set_aspect(1)
axes.add_artist(circle1)
plt.title('Circle')
plt.show()