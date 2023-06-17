import random

def creatingMatrix():
  matrix = []
  for i in range(4):
    lines = []
    for j in range(3):
      num = random.randint(1,15)
      lines.append(num)
    matrix.append(lines)
  return matrix

matrix_for_pairs_sum = creatingMatrix()

print(matrix_for_pairs_sum)

def sumOfPairs(matrix):
  matrix_sum = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] % 2 == 0:
        matrix_sum += matrix[i][j]
  return matrix_sum

sumOfPairs(matrix_for_pairs_sum)