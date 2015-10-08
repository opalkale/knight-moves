class Matrix:
  # Given a list of list of lines, creates a matrix.
  def __init__(self, list_of_lines):
    self.squares = []

    row = 0
    for line in list_of_lines:
      row += 1
      column = 0
      for letter in line:
        column += 1
        square = Square(row, column, letter)
        self.squares.append(square)


  # Prints all the squares in the matrix
  def print_squares(self):
    for square in self.squares:
      print(square.position, square.letter)

  # Returns all the knight moves given a position
  def possible_moves(self, row, column):
    all_moves = [
      self.square_with_position(row + 1, column + 2),
      self.square_with_position(row + 1, column - 2),
      self.square_with_position(row - 1, column + 2),
      self.square_with_position(row - 1, column - 2),
      self.square_with_position(row + 2, column + 1),
      self.square_with_position(row + 2, column - 1),
      self.square_with_position(row - 2, column + 1),
      self.square_with_position(row - 2, column - 1)
      ]

    possible_moves = []
    for move in all_moves:
      if move != False:
        possible_moves.append(move)
    return possible_moves

  # Returns a list of squares in the matrix with a given letter.
  def squares_with_letter(self, letter):
    squares_list = []
    for square in self.squares:
      if letter == square.letter:
        squares_list.append(square)
        #print(square.row, square.column)
    return squares_list

  # Returns the square in the matrix with a given position
  def square_with_position(self, row, column):
    for square in self.squares:
      if [row, column] == square.position:
        return square
    return False

class Square:
  # Squares have position and a letter at that position.
  def __init__(self, row, column, letter):
    self.row = row
    self.column = column
    self.letter = letter
    self.position = [row,column]

def knight_moves(matrix, word):
    if len(word) == 0:
      return True

    elif len(word) == 1:
      squares_with_letter = matrix.squares_with_letter(word)
      if squares_with_letter != None:
        return True

    else:
      squares_with_letter = matrix.squares_with_letter(word[0])
      if squares_with_letter != None:
        for square in squares_with_letter:
          possible_moves = matrix.possible_moves(square.row, square.column)
          for move in possible_moves:
            if move != False:
              if move.letter == word[1]:
                return knight_moves(matrix, word[1:])




def main():
  
  matrix_file = open("matrix.txt", "r")
  matrix_list = matrix_file.read().split("\n")
  matrix_list.remove('')

  # Creating matrix.
  matrix = Matrix(matrix_list)

  # Word to be looked for in matrix.
  word_file = open("wordlist.txt", "r")
  words_list = word_file.read().split("\r\n")
  words_list.remove('')

  list_answers = []
  for word in words_list:
    answer = knight_moves(matrix, words_list)
    if answer == True:
      list_answers.append(word)
  print(list_answers)

main()