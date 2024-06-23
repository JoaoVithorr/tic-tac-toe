# Definindo a proporção do tabuleiro 
BOARD_SIZE = 3

# Criando a classe do tabuleiro 
class Board: 
  
  def __init__(self):
    self.board = [["1", "2", "3"],
                  ["4", "5", "6"],
                  ["7", "8", "9"]]
    
  
  def is_valid_position(self, position):
    x, y = position_to_xy(position)
    return self.board[y][x] != "X" and self.board[y][x] != "O"


  def play(self, symbol, position):
    x, y = position_to_xy(position)
    self.board[y][x] = symbol


# Conferindo se há um ganhador
  def check_winning_positions(self):
    # check rows
    # [X, O, X] -> set([X, O, X]) = [X, O]
    for row in self.board:
      # Transformando em um set a lista, para identificar se há diferentes símbolos
      if len(set(row)) == 1:
        return True
        
    # check cols
    for x in range(BOARD_SIZE):
      col = []
      for y in range(BOARD_SIZE):
        col.append(self.board[y][x])
      if len(set(col)) == 1:
        return True
    
    # check diagonals
    diagonal_princ = []
    diagonal_sec = []


    for i in range(BOARD_SIZE):
      diagonal_princ.append(self.board[i][i])
      # diagonal principal = [0][0] [1][1] [2][2] 

      diagonal_sec.append(self.board[i][BOARD_SIZE - i - 1]) 
      # diagonal secundária = [0][2] [1][1] [2][0]
      

    if len(set(diagonal_princ)) == 1 or len(set(diagonal_sec)) == 1:
      return True 
    
    # Conferindo empate
  def check_draw_positions(self):
    for position in range(1, BOARD_SIZE * BOARD_SIZE + 1):
        if self.is_valid_position(position):
            return False  # Se encontrar uma posição válida, retorna False imediatamente
    return True  # Se percorrer todas as posições e não encontrar nenhuma válida, retorna True
        

# Transformando a posição(casa) em uma posição [x][y]
def position_to_xy(position):
  x = (position - 1) % 3
  y = (position - 1) // 3
  return x, y


