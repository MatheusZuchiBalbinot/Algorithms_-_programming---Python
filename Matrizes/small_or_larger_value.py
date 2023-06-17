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

smaller_or_bigger_value_of_a_Matrix = creatingMatrix()

def minValue(matrix):
  lower = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      lower.append(matrix[i][j])
  return(min(lower))

def maxValue(matrix):
  larger = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      larger.append(matrix[i][j])
  return(max(larger))

maxResult = maxValue(smaller_or_bigger_value_of_a_Matrix)
minResult = minValue(smaller_or_bigger_value_of_a_Matrix)

print(smaller_or_bigger_value_of_a_Matrix)
print(maxResult)
print(minResult)