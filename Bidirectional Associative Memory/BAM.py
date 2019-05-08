
import numpy as np
# initialization of 6x1 matrices
A1 = [[1],
     [-1],
     [-1],
     [1],
     [-1],
     [-1]]

A2 = [[-1],
      [1],
      [-1],
      [-1],
      [1],
      [-1]]

A3 = [[-1],
      [-1],
      [1],
      [-1],
      [-1],
      [1]]

# initialization of 3x1 matrices
B1 = [[-1],
      [1],
      [-1]]

B2 = [[1],
      [-1],
      [-1]]

B3 = [[-1],
      [-1],
      [1]]

M1 = np.matmul(A1, np.transpose(B1))  # calculation of A1 * B1(transposed)
M2 = np.matmul(A2, np.transpose(B2))  # calculation of A2 * B2(transposed)
M3 = np.matmul(A3, np.transpose(B3))  # calculation of A3 * B3(transposed)
print('M1: A1*B1 Matrix \n', M1)
print('M2: A2*B2 Matrix \n', M2)
print('M3: A3*B3 Matrix \n', M3)

M1M2 = np.add(M1, M2)  #calculation of matrices M1 + M2

# calculation of correlation matrix by adding M1, M2 and M3
M = np.add(M1M2, M3)  
print('M: Correlation Matrix \n', M)

MT = np.transpose(M)  # transposing correlation matrix
print('MT: Correlation Matrix (transposed) \n', MT)







