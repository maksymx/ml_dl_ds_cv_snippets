import scipy as sp
import scipy.integrate as integrate
from scipy.integrate import dblquad
from scipy import signal

result = integrate.quad(lambda x: x, 0, 4.5)
print(result[0])