O = input()

def creatingMatrix(l, c):
  matrix = []
  for i in range(l):
    lines = []
    for j in range(c):
      num = float(input())
      lines.append(num)
    matrix.append(lines)
  return matrix

below_main_diagonal = creatingMatrix(12,12)

matrix_sum = 0
matrix_count = 0

for i in range(len(below_main_diagonal)):
    for j in range(len(below_main_diagonal)):
        for x in range(11):
            for y in range(11-x):
                matrix_sum += below_main_diagonal[x][y]
                matrix_count += 1

if O == "S":
  print(matrix_sum)
elif O == "M":
  print(f"{matrix_sum/matrix_count:.1f}")