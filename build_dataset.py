import random
import pickle

EDGE = [[0,0],[1,1]]    # 0 0
                        # 1 1

CORNER = [[1,1],[1,0]]  # 1 1
                        # 1 0

DOT = [[1,0],[0,0]]     # 1 0
                        # 0 0

DGNL = [[1,0],[0,1]]    # 1 0
                        # 0 1

def rotate(shape, turn_n):
    if turn_n == 0:
        return shape

    new_shape = [[shape[1][0], shape[0][0]], [shape[1][1], shape[0][1]]]

    return rotate(new_shape, turn_n - 1)


edges = [rotate(EDGE, i) for i in range(4)]
corners = [rotate(CORNER, i) for i in range(4)]
dots = [rotate(DOT, i) for i in range(4)]
dgnls = [rotate(DGNL, i) for i in range(2)]

dataset = []


for shape in corners:
    dataset.append([shape, 0])

for shape in dots:
    dataset.append([shape, 0])

for shape in dgnls:
    # Add each diagonal twice, as there are only 2
    dataset.append([shape, 0])  
    dataset.append([shape, 0])

for shape in edges:
    # Add each edge 3 times, to have equal numbers edges/non-edges
    dataset.append([shape, 1])
    dataset.append([shape, 1])
    dataset.append([shape, 1])

random.shuffle(dataset)

pickle.dump(dataset, open('clear_edges_data.pickle', 'wb'))
