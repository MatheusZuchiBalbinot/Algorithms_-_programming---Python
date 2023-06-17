import random

def creatingMatrices():
  matrices = []
  for i in range(4):
    lines = []
    for j in range(3):
      num = random.randint(1,15)
      lines.append(num)
    matrices.append(lines)
  return matrices

matrices_A = creatingMatrices()
matrices_B = creatingMatrices()

print(matrices_A)
print(matrices_B)

def sumOfMatrizs(matrices_A, matrices_B):
  sum_matrices = []
  for i in range(len(matrices_A)):
    lines = []
    for j in range(len(matrices_A[0])):
      matrices_c = matrices_A[i][j] + matrices_B[i][j]
      lines.append(matrices_c)
    sum_matrices.append(lines)
  return sum_matrices

result = sumOfMatrizs(matrices_A, matrices_B)
print(result)