import random

class Game:
    def __init__(self):
        self.board = self.generate_board()
        self.flipped = [[False for i in range(5)] for i in range(5)]
        self.points = 0
        self.lost = False

    def flip(self, c1, c2):
        if self.flipped[c1][c2]:
            print("Error! This cell has already been flipped.")
        elif self.board[c1][c2] == 'V':
            self.lost = True
        else:
            self.points += self.board[c1][c2]
        self.flipped[c1][c2] = True

    def generate_board(self):
        board = [[0 for _ in range(5)] for _ in range(5)]
        numbers = [1, 2, 3]
        for i in range(5):
            for j in range(5):
                if random.random() < 0.2:  # 20% chance for Voltorb
                    board[i][j] = 'V'
                else:
                    board[i][j] = random.choice(numbers)
        return board
    
    def check_game_won(self):
        for i in range(5):
            for j in range(5):
                if not self.flipped[i][j] and self.board[i][j] != 'V':
                    return False
        return True

    def display_board(self):
        print("    0  1  2  3  4")
        for i in range(5):
            voltorbs_row = sum(1 for j in range(5) if self.board[i][j] == 'V')
            points_row = sum(self.board[i][j] for j in range(5) if isinstance(self.board[i][j], int))
            flipped_points_row = sum(self.board[i][j] for j in range(5) if self.flipped[i][j] and isinstance(self.board[i][j], int))
            flipped_cards_row = sum(1 for j in range(5) if self.flipped[i][j])
            print(f"{i}  ", end="")
            for j in range(5):
                if self.flipped[i][j]:
                    print(f"[{self.board[i][j]}]", end=" ")
                else:
                    print("[ ]", end=" ")
            print(f"   (V: {voltorbs_row}, P: {points_row}, Flipped: {flipped_cards_row}, Flipped Points: {flipped_points_row})")
        
        print("   ", end="")
        for j in range(5):
            voltorbs_col = sum(1 for i in range(5) if self.board[i][j] == 'V')
            points_col = sum(self.board[i][j] for i in range(5) if isinstance(self.board[i][j], int))
            flipped_points_col = sum(self.board[i][j] for i in range(5) if self.flipped[i][j] and isinstance(self.board[i][j], int))
            flipped_cards_col = sum(1 for i in range(5) if self.flipped[i][j])
            print(f"   (V: {voltorbs_col}, P: {points_col}, Flipped: {flipped_cards_col}, Flipped Points: {flipped_points_col})", end="")
        print()

    def display_progress(self):
        print(f"Points: {self.points}")
        print("Board:")
        self.display_board()
        print(self.display_row_col_info())  # Add this line to display row and column information
        if self.lost:
            print("Game Over! You hit a Voltorb.")

    def display_row_col_info(self):
        row_info = "Row Information:\n"
        for i in range(5):
            voltorbs_row = sum(1 for j in range(5) if self.flipped[i][j] and self.board[i][j] == 'V')
            points_row = sum(self.board[i][j] for j in range(5) if self.flipped[i][j] and isinstance(self.board[i][j], int))
            row_info += f"Row {i}: Voltorbs: {voltorbs_row}, Points: {points_row}\n"
        
        col_info = "\nColumn Information:\n"
        for j in range(5):
            voltorbs_col = sum(1 for i in range(5) if self.flipped[i][j] and self.board[i][j] == 'V')
            points_col = sum(self.board[i][j] for i in range(5) if self.flipped[i][j] and isinstance(self.board[i][j], int))
            col_info += f"Column {j}: Voltorbs: {voltorbs_col}, Points: {points_col}\n"
        
        return row_info + col_info


if __name__ == "__main__":
    def play_game():
        game = Game()
        game.display_progress()
        while not game.lost and not game.check_game_won():
            print("\nEnter the coordinates to flip a cell (row column):")
            try:
                row, col = map(int, input().split())
                if 0 <= row < 5 and 0 <= col < 5:
                    game.flip(row, col)
                    game.display_progress()
                else:
                    print("Invalid coordinates. Please enter numbers between 0 and 4.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")
        
        if game.lost:
            print("Game Over! You hit a Voltorb.")
        else:
            print("Congratulations! You've won the game!")

    play_game()
