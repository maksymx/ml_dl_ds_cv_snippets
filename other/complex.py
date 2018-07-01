import scipy as sp
from scipy import linalg


def norm(start, end, elem_numb):
    xs = sp.linspace(start, end, elem_numb)
    return linalg.norm(xs)

print(norm(2, 3, 100))