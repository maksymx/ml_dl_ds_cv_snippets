import scipy as sp

x = sp.random.random()
print("Random number: ", x)

x_square_root = sp.sqrt(x)
print("Square root: ", x_square_root)

matrix = sp.random.random(3)
print('Random matrix: ', matrix)

matrix = sp.append(matrix, sp.random.random(2))
print('New matrix: ', matrix)
