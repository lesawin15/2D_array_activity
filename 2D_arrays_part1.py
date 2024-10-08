#Uncomment each challenge as needed to demonstrate
#code running to students.

def main():

  #Challenge 1
  starter_board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ]

  #Show Starter Grid
  print("Starter Grid")
  print_grid(starter_board)
  print()

  #Show Challenge 1
  #challenge_1(starter_board)
  #print_info(1, starter_board)

  #Show Challenge 2
  #challenge_2(starter_board)
  #print_info(2, starter_board)

  #Show Challenge 3
  #challenge_3(starter_board)
  #print_info(3, starter_board)
  
  #Show Challenge 4
  #challenge_4(starter_board)
  #print_info(4, starter_board)
  
#print formatted grid
def print_grid(board):
  for row in board:
    print(row)

#reset grid to all 0s
def reset_grid(board):
  for row in range(4):
    for col in range(5):
      board[row][col] = 0

#print info and grid for each challenge and reset grid
def print_info(num, board):
  print(f"Challenge {num}")
  print_grid(board)
  print()
  reset_grid(board)

#counting up left to right
def challenge_1(board):
  new_value = 0
  for row in range(4):
    for col in range(5):
      board[row][col] = new_value
      new_value += 1

#counting up left to right - spaces restricted
def challenge_2(board):
  new_value = 0
  for row in range(3):
    for col in range(2):
      board[row][col] = new_value
      new_value += 1

#mod pattern
def challenge_3(board):
  for row in range(4):
    for col in range(5):
      new_value = (row + 1) % (col + 1)
      board[row][col] = new_value

#double first num in each row
def challenge_4(board):
  new_value = 0
  for row in range(4):
    for col in range(5):
      board[row][col] = new_value
      new_value += 1
    new_value *= 2

main()