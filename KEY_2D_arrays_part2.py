#KEY

#Scroll down to helper functions to see solutions to each challenge

def main():

  #Challenge 1
  starter_board_1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]

  col_count(starter_board_1)
  print("Challenge 1")
  print_grid(starter_board_1)
  print()

  #Challenge 2
  starter_board_2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]

  diagonal_ones(starter_board_2)
  print("Challenge 2")
  print_grid(starter_board_2)
  print()

  #Challenges 3-5
  seven_board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 7, 3, 0],
                 [0, 5, 0, 0, 0]]

  print_grid(seven_board)
  print()

  #Challenge 3
  print("Challenge 3")
  locate_seven(seven_board)
  print()

  #Challenge 4
  print("Challenge 4")
  right_of_seven(seven_board)
  print()

  #Challenge 5
  print("Challenge 5")
  lower_left_diagonal_seven(seven_board)
  print()


def print_grid(board):
  for row in board:
    print(row)

#Challenge 1
def col_count(board):
  new_val = 0
  for col in range(5):
    for row in range(4):
      board[row][col] = new_val
      new_val += 1
  return


#Challenge 2
def diagonal_ones(board):
  for row in range(4):
    for col in range(5):
      if row == col:
        board[row][col] = 1
  return

#can do this with less code and only one loop
  #for row in range(4):
    #since row and col are equal, can write like this
    #board[row][row] = 1


#Challenge 3 - print location of 7 (row and col)
def locate_seven(board):
  for row in range(4):
    for col in range(5):
      if board[row][col] == 7:
        print(f"row: {row + 1}")
        print(f"col: {col + 1}")
  return


#Challenge 4 - print value to the right of 7
def right_of_seven(board):
  for row in range(4):
    for col in range(5):
      if board[row][col] == 7:
        right_value = board[row][col + 1]
        print(right_value)
  return


#Challenge 5 - print value diagonally left and down from 7
def lower_left_diagonal_seven(board):
  for row in range(4):
    for col in range(5):
      if board[row][col] == 7:
        right_value = board[row + 1][col - 1]
        print(right_value)
  return


main()
