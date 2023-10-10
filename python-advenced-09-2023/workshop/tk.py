import tkinter as tk

def start_game(window, player_one, player_two):
    window

def start_screen():
    window = tk.Tk()
    window.geometry('240x240')
    window.title('Tic Tac Toe')
    window.configure(background='red')

    tk.Label(window, text='First name player name: ', bg='black', fg='blue').pack()
    player_one = tk.Entry(window)
    player_one.pack()

    tk.Label(window, text='Second name player name: ', bg='black', fg='blue').pack()
    player_two = tk.Entry(window)
    player_two.pack()

    tk.Button(window, text='Start game', command=lambda: start_game(window, player_one)).pack()

    window.mainloop()

if __name__ == '__main__':
    start_screen()

