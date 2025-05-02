# import tkinter as tk
# from    tkinter import messagebox
#
# window = tk.Tk()
# window.title("Крестики-нолики")
# window.geometry("300x350")
#
# current_player = "X"
# buttons = []
#
#
# def check_winner():
#     for i in range(3):
#         if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] !="":
#             return True
#         if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] !="":
#             return True
#
#     if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] !="":
#             return True
#     if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] !="":
#             return True
#     return False
#
#
# def on_click(row, col):
#     global current_player
#     button = buttons[row][col]
#     if button["text"] == "":
#         button["text"] = current_player
#         if check_winner():
#            messagebox.showinfo(f"Game over",
#                             f"player {current_player} wins!")
#            window.quit()
#         else:
#            current_player = "0" if current_player == "X" else "X"
#
#
# for i in range(3):
#     row = []
#     for j in range(3):
#         btn = tk.Button(window,text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r,c))
#         btn.grid(row=i, column=j)
#         row.append(btn)
#     buttons.append(row)
#
# window.mainloop()

import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.geometry("330x400")

        # Настройки игры
        self.current_player = "X"
        self.player1_score = 0
        self.player2_score = 0
        self.game_count = 0
        self.player1_name = "Игрок 1 (X)"
        self.player2_name = "Игрок 2 (O)"

        # Создаем интерфейс
        self.create_menu()
        self.create_scoreboard()
        self.create_board()
        self.create_reset_button()

        self.window.mainloop()

    def create_menu(self):
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.grid(row=0, column=0, columnspan=3, pady=10)

        tk.Label(self.menu_frame, text="Режим игры:", font=("Arial", 12)).pack(side=tk.LEFT)

        # Поле для ввода имен игроков
        self.name_frame = tk.Frame(self.window)
        self.name_frame.grid(row=1, column=0, columnspan=3, pady=5)

        tk.Label(self.name_frame, text="Игрок 1:", font=("Arial", 10)).pack(side=tk.LEFT)
        self.player1_entry = tk.Entry(self.name_frame, width=15)
        self.player1_entry.pack(side=tk.LEFT, padx=5)
        self.player1_entry.insert(0, "Игрок 1")

        tk.Label(self.name_frame, text="Игрок 2:", font=("Arial", 10)).pack(side=tk.LEFT, padx=(10, 0))
        self.player2_entry = tk.Entry(self.name_frame, width=15)
        self.player2_entry.pack(side=tk.LEFT, padx=5)
        self.player2_entry.insert(0, "Игрок 2")

        # Кнопка применения имен
        self.apply_names_btn = tk.Button(self.window, text="Применить имена",
                                         command=self.update_player_names,
                                         font=("Arial", 10), bg="#2196F3", fg="white")
        self.apply_names_btn.grid(row=2, column=0, columnspan=3, pady=5)

    def update_player_names(self):
        name1 = self.player1_entry.get() or "Игрок 1"
        name2 = self.player2_entry.get() or "Игрок 2"
        self.player1_name = f"{name1} (X)"
        self.player2_name = f"{name2} (O)"
        self.update_scoreboard()

    def create_scoreboard(self):
        self.score_frame = tk.Frame(self.window)
        self.score_frame.grid(row=3, column=0, columnspan=3, pady=5)

        self.player1_label = tk.Label(self.score_frame,
                                      text=f"{self.player1_name}: {self.player1_score}",
                                      font=("Arial", 10))
        self.player1_label.pack(side=tk.LEFT, padx=10)

        self.vs_label = tk.Label(self.score_frame, text="vs", font=("Arial", 10))
        self.vs_label.pack(side=tk.LEFT, padx=5)

        self.player2_label = tk.Label(self.score_frame,
                                      text=f"{self.player2_name}: {self.player2_score}",
                                      font=("Arial", 10))
        self.player2_label.pack(side=tk.LEFT, padx=10)

    def create_board(self):
        self.board_frame = tk.Frame(self.window)
        self.board_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(self.board_frame, text="", font=("Arial", 24), width=3, height=1,
                                bg="#f0f0f0", activebackground="#e0e0e0",
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)
                row.append(btn)
            self.buttons.append(row)

    def create_reset_button(self):
        self.reset_btn = tk.Button(self.window, text="Новая игра", font=("Arial", 12),
                                   command=self.reset_game, bg="#4CAF50", fg="white")
        self.reset_btn.grid(row=5, column=0, columnspan=3, pady=10, ipadx=10, ipady=5)

        self.reset_series_btn = tk.Button(self.window, text="Сбросить счёт", font=("Arial", 10),
                                          command=self.reset_series, bg="#FF5722", fg="white")
        self.reset_series_btn.grid(row=6, column=0, columnspan=3, pady=5, ipadx=5, ipady=2)

    def update_scoreboard(self):
        self.player1_label.config(text=f"{self.player1_name}: {self.player1_score}")
        self.player2_label.config(text=f"{self.player2_name}: {self.player2_score}")

    def on_click(self, row, col):
        button = self.buttons[row][col]

        if button["text"] == "":
            button["text"] = self.current_player
            button.config(fg="blue" if self.current_player == "X" else "red")

            if self.check_winner():
                winner_name = self.player1_name if self.current_player == "X" else self.player2_name
                if self.current_player == "X":
                    self.player1_score += 1
                else:
                    self.player2_score += 1

                self.game_count += 1
                self.update_scoreboard()

                if self.player1_score >= 3 or self.player2_score >= 3:
                    final_winner = self.player1_name if self.player1_score >= 3 else self.player2_name
                    messagebox.showinfo("Конец игры!",
                                        f"{final_winner} победил в серии из {self.game_count} игр!")
                    self.reset_series()
                else:
                    messagebox.showinfo("Победа!", f"{winner_name} победил!")
                    self.reset_game()
            elif self.is_board_full():
                self.game_count += 1
                messagebox.showinfo("Ничья!", "Ничья!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_turn_indicator()

    def update_turn_indicator(self):
        current_name = self.player1_name if self.current_player == "X" else self.player2_name
        self.vs_label.config(text=f"Ход: {current_name[-2]}")

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def is_board_full(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
                button.config(bg="#f0f0f0")

        self.current_player = "X"
        self.update_turn_indicator()

    def reset_series(self):
        self.player1_score = 0
        self.player2_score = 0
        self.game_count = 0
        self.update_scoreboard()
        self.reset_game()


if __name__ == "__main__":
    game = TicTacToe()