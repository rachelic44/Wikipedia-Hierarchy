import pickle
import itertools
import os

abstract_algebra = pickle.load(open(os.path.join('small_graph', 'AbstractAlgebraIDs.pkl'), 'rb'))
binary_arithmetic = pickle.load(open(os.path.join('small_graph', 'BinaryArithmeticIDs.pkl'), 'rb'))
computer_arithmetic = pickle.load(open(os.path.join('small_graph', 'ComputerArithmeticIDs.pkl'), 'rb'))
linear_algebra = pickle.load(open(os.path.join('small_graph', 'LinearAlgebraIDs.pkl'), 'rb'))
g = pickle.load(open(os.path.join('small_graph', 'GraphAsNetworkx.pkl'), 'rb'))

discipline_to_idx = {"Math": 0, "Algebra": 1, "Arithmetics": 2, "AbstractAlgebra": 3, "LinearAlgebra": 4,
                     "BinaryArithmetic": 5, "ComputerArithmetic": 6}
labels_dict = {(0, 0): (0, 0, 0), (0, 1): (0, 1, 0), (0, 2): (0, 1, 0), (0, 3): (0, 2, 0), (0, 4): (0, 2, 0),
               (0, 5): (0, 2, 0), (0, 6): (0, 2, 0), (1, 0): (0, 1, 0), (1, 1): (0, 0, 1), (1, 2): (1, 1, 0),
               (1, 3): (0, 1, 1), (1, 4): (0, 1, 1), (1, 5): (1, 2, 0), (1, 6): (1, 2, 0), (2, 0): (1, 0, 0),
               (2, 1): (1, 1, 0), (2, 2): (0, 0, 1), (2, 3): (1, 2, 0), (2, 4): (1, 2, 0), (2, 5): (0, 1, 1),
               (2, 6): (0, 1, 1), (3, 0): (2, 0, 0), (3, 1): (1, 0, 1), (3, 2): (2, 1, 0), (3, 3): (0, 0, 2),
               (3, 4): (1, 1, 1), (3, 5): (2, 2, 0), (3, 6): (2, 2, 0), (4, 0): (2, 0, 0), (4, 1): (1, 0, 1),
               (4, 2): (2, 1, 0), (4, 3): (1, 1, 1), (4, 4): (0, 0, 2), (4, 5): (2, 2, 0), (4, 6): (2, 2, 0),
               (5, 0): (2, 0, 0), (5, 1): (2, 1, 0), (5, 2): (1, 0, 1), (5, 3): (2, 2, 0), (5, 4): (2, 2, 0),
               (5, 5): (0, 0, 2), (5, 6): (1, 1, 1), (6, 0): (2, 0, 0), (6, 1): (2, 1, 0), (6, 2): (1, 0, 1),
               (6, 3): (2, 2, 0), (6, 4): (2, 2, 0), (6, 5): (1, 1, 1), (6, 6): (0, 0, 2)}
pickle.dump(labels_dict, open('labels.pkl', 'wb'))