import random

class World:
  def __init__(self, rows, cols, data):
    self.rows = rows
    self.cols = cols
    self.data = data

def void_world(rows, cols):
  return World(rows,cols,[[0 for i in range(cols)] for j in range(rows)])

def random_world(rows, cols):
  return World(rows,cols,[[random.getrandbits(1) for i in range(cols)] for j in range(rows)])


def count_neighbors(world, x, y):
  sum = 0
  for i in [-1,0,1]:
    for j in [-1,0,1]:
      row = (x + i + world.rows) % world.rows
      col = (y + j + world.cols) % world.cols
      sum += world.data[row][col]
  sum -= world.data[x][y]
  return sum

def next_generation(world):
  next = void_world(world.rows,world.cols)

  for i in range(world.rows):
    for j in range(world.cols):
      current_cell = world.data[i][j]

      neighbors = count_neighbors(world, i, j)

      if (current_cell == 0 and neighbors == 3):
        next.data[i][j] = 1
      elif (current_cell == 1 and (neighbors < 2 or neighbors > 3)):
        next.data[i][j] = 0
      else :
        next.data[i][j] = current_cell

  return next
      
