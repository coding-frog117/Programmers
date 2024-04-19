import sys

originSudoku = []
for i in range(9):
  arr = list(map(int,sys.stdin.readline().split()))
  originSudoku.append(arr)

def checkWhichZone(index):
    if (index < 3):
      return [0,1,2]
    if (index >= 3 and index < 6):
      return [3,4,5]
    if (index >= 6):
      return [6,7,8]

def findEmptyIndex(array):
  for i in range(9):
    for j in range(9):
      if (array[i][j] ==0):
        return i,j
  return 9,9

# col check
def col_check(sudoku,i,num):
  if (num in sudoku[i]):
    return False
  return True

# row check
def row_check(sudoku,j,num):
  for i in range(9):
    if (num == sudoku[i][j]):
      return False
  return True

# 3*3 matrix check
def matrix_check(i,j,num):
  rowZone = checkWhichZone(i)
  colZone = checkWhichZone(j)

  for row in rowZone:
    for col in colZone:
      if (sudoku[row][col] == num):
        return False
  return True

def BT(i,j,num,sudoku):
  if (col_check(sudoku,i,num) and row_check(sudoku,j,num) and matrix_check(i,j,num)):
    sudoku[i][j] = num

  else :
    return False
  nextcol,nextrow = findEmptyIndex(sudoku)

  if (nextcol == 9 and nextrow == 9) :
    global originSudoku
    originSudoku = sudoku
    for subArray in originSudoku:
      print(' '.join(map(str,subArray)))
    
    return True
  
  for x in range(9):
    if (BT(nextcol,nextrow ,x+1,sudoku)):
      return True

  sudoku[i][j] = 0
  return False

sudoku = originSudoku[:]
col,row = findEmptyIndex(sudoku)

for i in range(9):
  BT(col,row,i+1,sudoku)