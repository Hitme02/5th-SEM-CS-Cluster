class TicTacToe:
    def __init__(self):
        # Step 1: Initialize the board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'  # AI player

    def print_board(self):
        # Step 2: Print the board
        for row in self.board:
            print(' | '.join(row))
            print('-' * 5)

    def is_draw(self):
        # Check if the game is a draw
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def is_game_over(self, board=None):
        if board is None:
            board = self.board  # Default to the current board state
        # Check rows
        for row in board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                return row[0]
        # Check columns
        for col in zip(*board):
            if col.count(col[0]) == len(col) and col[0] != ' ':
                return col[0]
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]
        return False

    def dfs(self, board, depth, player):
        # Step 5: DFS logic to choose the best move
        winner = self.is_game_over(board)
        if winner:
            if winner == 'X':  # AI wins
                return {'score': 1}
            else:  # Human wins
                return {'score': -1}
        elif self.is_draw():
            return {'score': 0}  # Draw

        if player == 'X':
            best = {'score': -float('inf')}
            symbol = 'X'
        else:
            best = {'score': float('inf')}
            symbol = 'O'

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = symbol
                    score = self.dfs(board, depth + 1, 'O' if player == 'X' else 'X')
                    board[i][j] = ' '
                    score['row'] = i
                    score['col'] = j

                    if player == 'X':  # Maximize for AI
                        if score['score'] > best['score']:
                            best = score
                    else:  # Minimize for opponent
                        if score['score'] < best['score']:
                            best = score
        return best

    def play(self):
        # Game loop
        while True:
            self.print_board()
            winner = self.is_game_over()
            if winner or self.is_draw():
                print("Game Over.")
                if self.is_draw():
                    print("It's a draw!")
                else:
                    print(f"Player {winner} wins!")
                break

            if self.player == 'X':
                print("AI is making a move...")
                best_move = self.dfs(self.board, 0, 'X')
                self.board[best_move['row']][best_move['col']] = 'X'
            else:
                # Step 4: Accept keyboard input for 'O'
                while True:
                    try:
                        row = int(input("Enter the row number (0-2): "))
                        col = int(input("Enter the column number (0-2): "))
                        if self.board[row][col] == ' ':
                            self.board[row][col] = 'O'
                            break
                        else:
                            print("Invalid move. Try again.")
                    except (ValueError, IndexError):
                        print("Invalid input. Please enter numbers between 0 and 2.")

            self.player = 'O' if self.player == 'X' else 'X'


game = TicTacToe()
game.play()