from itertools import permutations
from tkinter import *
import matplotlib.pyplot as plt
import networkx as nx

Graph = nx.Graph()
edges = []


def dist(point1, point2):
    """
    Returns the Euclidean distance of two points in the Cartesian Plane.

    >>> distance([3,4],[0,0])
    5.0
    >>> distance([3,6],[10,6])
    7.0
    """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5


def total_distance(points):
    """
    Returns the length of the path passing through
    all the points in the given order.

    >>> total_distance([[1,2],[4,6]])
    5.0
    >>> total_distance([[3,6],[7,6],[12,6]])
    9.0
    >>> total_distance([(100, 300), (300, 100), (400, 100), (500, 100), (600, 200), (600, 350), (700, 400), (900, 200)])
    1168.9101800615372
    """
    return sum([dist(point, points[index + 1]) for index, point in enumerate(points[:-1])])


#testcase
A = [(100, 300), (200, 600)]
B = [(200, 100), (600, 600)]
C = [(500, 300), (200, 600)]
D = [(500, 200), (400, 600)]
E = [(300, 100), (600, 600)]

r1 = (100, 600)
r2 = (600, 600)


trips = [A, B, C, D]
perm = permutations(trips)

# for t in trips:
#     print(t, dist(*t))
#
# for p in perm:
#     # print(*p,sep='\n')
#     for t in p:
#         print(*t,sep='\n')


# print(*perm, sep='\n')

for p in perm:
    path = [r1]
    for t in p:
        path.append(t[0])
        path.append(t[1])
    print(path, sep='\n')
    print(total_distance(path))



# #GUI
# canvas = Canvas(width=1400, height=700)
# canvas.configure(background='white')
# canvas.pack(expand=YES, fill=BOTH)
#
# for t in trips:
#     canvas.create_line(*t[0], *t[1], width=2, arrow=LAST)
#
# mainloop()
