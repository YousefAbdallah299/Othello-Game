import tkinter as tk

from gameController import GameController


class View:
    def __init__(self, master):
        self.computer_button = None
        self.human_button = None
        self.hard_button = None
        self.medium_button = None
        self.easy_button = None
        self.human_vs_computer_button = None
        self.exit_button = None
        self.human_vs_human_button = None
        self.winner_label = None
        self.white_disks_label = None
        self.black_disks_label = None
        self.second_window = None
        self.buttons = []
        self.master = master
        self.curr_color = 'B'
        self.game_controller = GameController()
        self.cell_width = 100
        self.cell_height = 100
        self.canvas = tk.Canvas(master, width=800, height=800)
        self.draw_board()
        self.canvas.bind("<Button-1>", self.canvas_click)
        self.canvas.pack()
        self.rounds = 0

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                x1 = i * self.cell_width
                y1 = j * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
        self.updateGridStatus()

    def update(self, x, y, color):
        # print(f"Updating cell at ({x}, {y}) with color {color}")
        x1 = x * self.cell_width + 10
        y1 = y * self.cell_height + 10
        x2 = (x + 1) * self.cell_width - 10
        y2 = (y + 1) * self.cell_height - 10
        # print(f"Oval coordinates: ({x1}, {y1}), ({x2}, {y2})")
        self.canvas.create_oval(x1, y1, x2, y2, fill=color)
        # self.canvas.update()

    def updateGridStatus(self):
        grid = self.game_controller.board
        for i in range(8):
            for j in range(8):
                x1 = i * self.cell_width
                y1 = j * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")

        possibleMoves = self.game_controller.getValidMoves(self.game_controller.currentToken)
        for [x, y] in possibleMoves:
            self.update(y, x, "gray")
        for i in range(8):
            for j in range(8):
                if grid[i][j] == 'B':
                    self.update(j, i, "black")
                elif grid[i][j] == 'W':
                    self.update(j, i, "white")

    def create_score_window(self):
        self.second_window = tk.Toplevel(self.master)
        self.second_window.title("Score")
        self.second_window.geometry("400x400")

        self.black_disks_label = tk.Label(self.second_window)
        self.black_disks_label.pack()

        self.white_disks_label = tk.Label(self.second_window)
        self.white_disks_label.pack()

        self.winner_label = tk.Label(self.second_window)
        self.winner_label.pack()

        tk.Button(self.second_window, text="Close", command=self.second_window.withdraw).pack()

    def update_score_window(self):
        black_disks = self.game_controller.getPlayerDisks('B')
        white_disks = self.game_controller.getPlayerDisks('W')
        winner = self.game_controller.whoWins

        self.black_disks_label.config(text=f"Black Disks: {black_disks}")
        self.white_disks_label.config(text=f"White Disks: {white_disks}")
        self.winner_label.config(text=f"Winner: {winner}")

        self.second_window.deiconify()

    def print_menu(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.canvas.create_text(400, 100, text="Menu", font=("Helvetica", 100))

        self.human_vs_human_button = tk.Button(self.canvas, text="1. Human vs Human", command=self.human_vs_human,
                                               font=("Helvetica", 32))
        self.human_vs_human_button.place(x=200, y=200, width=450, height=100)
        self.buttons.append(self.human_vs_human_button)

        self.human_vs_computer_button = tk.Button(self.canvas, text="2. Human vs Computer",
                                                  command=self.human_vs_computer, font=("Helvetica", 32))
        self.human_vs_computer_button.place(x=200, y=350, width=450, height=100)
        self.buttons.append(self.human_vs_computer_button)

        self.exit_button = tk.Button(self.canvas, text="3. Exit", command=self.exit_game, font=("Helvetica", 32))
        self.exit_button.place(x=200, y=500, width=450, height=100)
        self.buttons.append(self.exit_button)

    def clear_buttons(self):
        for button in self.buttons:
            button.destroy()
        self.buttons = []

    def human_vs_human(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.game_controller.twoHumanMode = True
        self.game_controller.currentToken = 'B'
        self.draw_board()
        self.create_score_window()
        self.update_score_window()

    def human_vs_computer(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.game_controller.twoHumanMode = False
        self.difficulty_menu()

    def difficulty_menu(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.canvas.create_text(400, 100, text="Choose Difficulty", font=("Helvetica", 50))

        self.easy_button = tk.Button(self.canvas, text="1. Easy", command=self.easy, font=("Helvetica", 32))
        self.easy_button.place(x=200, y=200, width=450, height=100)
        self.buttons.append(self.easy_button)

        self.medium_button = tk.Button(self.canvas, text="2. Medium", command=self.medium, font=("Helvetica", 32))
        self.medium_button.place(x=200, y=350, width=450, height=100)
        self.buttons.append(self.medium_button)

        self.hard_button = tk.Button(self.canvas, text="3. Hard", command=self.hard, font=("Helvetica", 32))
        self.hard_button.place(x=200, y=500, width=450, height=100)
        self.buttons.append(self.hard_button)

    def who_first(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.canvas.create_text(400, 100, text="Who First", font=("Helvetica", 50))

        self.human_button = tk.Button(self.canvas, text="1. Human", command=self.human, font=("Helvetica", 32))
        self.human_button.place(x=200, y=200, width=450, height=100)
        self.buttons.append(self.human_button)

        self.computer_button = tk.Button(self.canvas, text="2. Computer", command=self.computer, font=("Helvetica", 32))
        self.computer_button.place(x=200, y=350, width=450, height=100)
        self.buttons.append(self.computer_button)

    def human(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.draw_board()
        self.create_score_window()
        self.update_score_window()
        self.game_controller.currentToken = 'B'
        self.game_controller.computerToken = 'W'

    def computer(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.game_controller.currentToken = 'B'
        self.game_controller.computerToken = 'B'
        self.game_controller.computer_play()
        self.draw_board()
        self.create_score_window()
        self.update_score_window()

    def easy(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.game_controller.difficulty = 1
        self.who_first()

    def medium(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.game_controller.difficulty = 3
        self.who_first()

    def hard(self):
        self.canvas.delete("all")
        self.clear_buttons()
        self.game_controller.difficulty = 5
        self.who_first()

    def exit_game(self):
        self.canvas.master.destroy()

    def canvas_click(self, event):
        if self.move(event):
            self.updateGridStatus()
            self.update_score_window()

    def move(self, event):
        cell_x = event.x // self.cell_width
        cell_y = event.y // self.cell_height
        self.game_controller.currX = cell_y
        self.game_controller.currY = cell_x

        # this is a human player move
        if self.game_controller.computerToken != self.game_controller.currentToken:
            # if is not a valid cell to click on it
            if not self.game_controller.valid_cell(self.game_controller.currX, self.game_controller.currY):
                return False
            else:
                print("Human Player color: ", self.game_controller.currentToken)
                # play the human game
                human_play = self.game_controller.human_play(self.game_controller.currentToken)
                computer_play = False
                if not self.game_controller.twoHumanMode:
                    computer_play = self.game_controller.computer_play()
                # if there is any new move on the board return true
                return human_play or computer_play


root = tk.Tk()
board = View(root)
board.print_menu()
root.mainloop()
