'''
This is not the most optimal way to do this. If we memoize the words, we can reduce the cost of the operations significantly.
'''
class Matrix:
  # Given a list of list of lines, creates a matrix consisting of squares.
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

  # Prints all the squares in the matrix.
  def print_squares(self):
    for square in self.squares:
      print(square.position, square.letter)

  # Returns all the possible knight moves given a position.
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
    return squares_list

  # Returns the square in the matrix with a given position.
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


# Given a matrix and a word, returns 'True' if the word is in matrix, and 'None' otherwise.
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

  # Removes empty strings from a list.
  def remove_empty_words(list_of_words):
    for word in list_of_words:
      if word == '':
        list_of_words.remove(word)
  
  # Reads from matrix.txt to create a list of letters that represent rows in a matrix.
  matrix_file = open("matrix.txt", "r")
  matrix_list = matrix_file.read().split("\n")
  remove_empty_words(matrix_list)

  # Reads from wordlist.txt to create a list of words.
  word_file = open("wordlist.txt", "r")
  word_list = word_file.read().split("\r\n")
  remove_empty_words(word_list)

  # Creates a matrix.
  matrix = Matrix(matrix_list)

  # Test matrix and words.
  '''
  test_matrix = Matrix([
    'QWERTNUI',
    'OPAADFGH',
    'TKLZXCVB',
    'NMRWFRTY',
    'UIOPASDF',
    'GHJOLZXC',
    'VBNMQWER',
    'TYUIOPAS'
    ])
  
  test_word_list = ["ALGOL", "FORTRAN", "SIMULA"]
  '''

  # Creates a list of all the words found in the matrix.
  words_found_in_matrix = []
  for word in word_list:
    found = knight_moves(matrix, word)
    if found == True:
      words_found_in_matrix.append(word)

  sorted(words_found_in_matrix)

  print("Found " + str(len(words_found_in_matrix)) + " words in the matrix")
  print("The first match is " + (words_found_in_matrix[0]) + " and the last match is " + (words_found_in_matrix[-1]))
  

main()