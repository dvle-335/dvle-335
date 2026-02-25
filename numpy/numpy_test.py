import numpy as np
from peak import new_file, peak_find, mass_convert, fit_func
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([1, 2, 3, 4, 5, 6, 7, 8])
c = [1,2,3]
print(len(c))
d = np.array([[1,2],[3,4],[5,6]])
print(d.shape[1])

massdata = new_file('collisionbg3(20022026)(1).txt')