import tkinter as tk
from tkinter import messagebox
import random
import math
import player

class Board():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    def get_board(self):
        return self.board
    
    def clear_board(self):
        self.board=[' ' for _ in range(9)]

    def make_move(self, square, letter,print=False):
        if self.board[square] == ' ':
            self.board[square] = letter
            if(print):
                self.print_board()
            if self.check_winner(letter):
                self.current_winner = letter
            return True
        return False
    
    def check_winner(self, mark):

        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]             # diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == mark for i in condition):
                self.winning_condition = condition
                return True
        return False
    
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print( "")

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

class play:
    color_blue = "#4584b6"
    color_yellow = "#ffde57"
    color_gray = "#343434"
    color_light_gray = "#646464"
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        # self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(background=play.color_gray)
        # open in center of screen
        # windowWidth = self.root.winfo_reqwidth()
        # windowHeight = self.root.winfo_reqheight()
        # positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
        # positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
        # self.root.geometry("+{}+{}".format(positionRight, positionDown))

        self.turn = ' '
        self.board= Board()
        
        self.main_menu()

    def main_menu(self):
        self.clear_frame()
        
        menu_frame = tk.Frame(self.root, background=play.color_gray)
        menu_frame.pack(padx=20, pady=50)
        
        title_label = tk.Label(menu_frame, text="Tic Tac Toe",foreground=play.color_blue,background=play.color_gray, font=("Consolas", 50, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        play_computer_btn = tk.Button(menu_frame, text="Play with Computer",foreground=play.color_blue, background=play.color_gray,font=("Consolas", 35, "bold"),command=self.play_computer)
        play_computer_btn.grid(row=1, column=0, padx=10, pady=5)
        
        play_player_btn = tk.Button(menu_frame, text="Multiplayer",foreground=play.color_blue,background=play.color_gray,font=("Consolas", 35, "bold"), command=self.play_player)
        play_player_btn.grid(row=2, column=0, padx=10, pady=5)
        
        about_creator_btn = tk.Button(menu_frame, text="About Creator",foreground=play.color_blue,background=play.color_gray,font=("Consolas", 35, "bold"), command=self.about_creator)
        about_creator_btn.grid(row=3, column=0, padx=10, pady=5)
        
        quit_btn = tk.Button(menu_frame, text="Quit",foreground=play.color_blue, background=play.color_gray,font=("Consolas", 35, "bold"),command=self.root.destroy)
        quit_btn.grid(row=4, column=0, padx=10, pady=5)
        
        self.current_frame = menu_frame

    def play_computer(self):
        self.new_game()
        self.player = 'X'
        self.computer = 'O'
        self.computer_player=player.SmartComputerPlayer("computer")
        self.turn = random.choice(['player', 'computer'])
        if self.turn == 'computer':
            self.computer_move()
            self.turn = 'player'
        self.label.config(text=self.turn+"'s turn")

    def play_player(self):
        self.new_game()
        self.player1 = 'X'
        self.player2 = 'O'
        self.turn = random.choice(['player1', 'player2'])
        self.label.config(text=self.turn+"'s turn")

    def new_game(self):
        self.clear_frame()
        self.board=Board()
        
        game_frame = tk.Frame(self.root)
        game_frame.pack(padx=20, pady=50)
        game_frame.configure(background=play.color_gray)

        self.label = tk.Label(game_frame, text=self.turn+"'s turn", font=("Consolas", 20), background=play.color_gray,
                    foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")
        
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(game_frame, text=' ', foreground=play.color_blue,background=play.color_gray,
                                font=("Consolas", 50, "bold"), width=4, height=1,command=lambda r=i, c=j: self.click(r, c))
                btn.grid(row=i+1, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        restartbtn = tk.Button(game_frame, text="restart", font=("Consolas", 20), background=play.color_gray,
                        foreground="white", command=self.new_game)
        restartbtn.grid(row=4, column=1, pady=20)

        back_btn = tk.Button(game_frame, text="Back",  font=("Consolas", 20), background=play.color_gray,
                        foreground="white",command=self.main_menu)
        back_btn.grid(row=4, column=2, pady=20)

        self.current_frame = game_frame

    def about_creator(self):
        messagebox.showinfo("About Creator", "This game was created by Hirok Reza.")

    def click(self, row, col):
        if self.turn == 'player1':
            mark = self.player1
            if self.board.make_move(row*3+col, mark):
                self.turn = 'player2'
                self.buttons[row][col].config(text=mark)
        elif self.turn == 'player2':
            mark = self.player2
            if self.board.make_move(row*3+col, mark):
                self.turn = 'player1'
                self.buttons[row][col].config(text=mark)
        elif self.turn == 'player':
            mark = self.player
            if self.board.make_move(row*3+col, mark):
                self.buttons[row][col].config(text=mark)
                if self.board.current_winner==None:
                    self.computer_move()


        if self.board.current_winner!=None:
            self.label.config(text=self.board.current_winner+" is the winner!", foreground=play.color_yellow)
            for i in self.board.winning_condition:
                self.buttons[i//3][i%3].config(foreground=play.color_yellow, background=play.color_light_gray)
            messagebox.showinfo("Tic Tac Toe", f"{self.board.current_winner} wins!")
            self.reset_board()
            return
        elif not self.board.empty_squares():
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            self.reset_board()
            return
        self.label.config(text=self.turn+"'s turn")

    def computer_move(self):
        move = self.computer_player.get_move(self.board)
        self.board.make_move(move, self.computer)
        self.buttons[move//3][move%3].config(text=self.computer)

    def reset_board(self):
        self.clear_frame()
        self.main_menu()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = play(root)
    root.mainloop()
