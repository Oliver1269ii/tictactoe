import random


def display_board():
    print(("+" + "-"*7)*3 + "+")
    print("|       "*3 + "|")
    print(f"|   {moves['m1']}   |   {moves['m2']}   |   {moves['m3']}   |")
    print("|       "*3 + "|")
    print(("+" + "-"*7)*3 + "+")
    print("|       "*3 + "|")
    print(f"|   {moves['m4']}   |   {moves['m5']}   |   {moves['m6']}   |")
    print("|       "*3 + "|")
    print(("+" + "-"*7)*3 + "+")
    print("|       "*3 + "|")
    print(f"|   {moves['m7']}   |   {moves['m8']}   |   {moves['m9']}   |")
    print("|       "*3 + "|")
    print(("+" + "-"*7)*3 + "+")


def enter_move():
    while True:
        user = int(input("Enter your guess: "))
        if user in free_squares:
            usersquares.append(user)
            del free_squares[free_squares.index(user)]
            moves[f"m{user}"] = "O"
            return user
        else:
            print("Already taken! Try again")


def victory_for(player_squares):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
        [1, 5, 9], [3, 5, 7]  # Diagonals
    ]

    for combo in winning_combinations:
        if all(square in player_squares for square in combo):
            return True
    return False


def draw_move():
    while True:
        cpu = random.choice(free_squares)
        if cpu in free_squares:
            del free_squares[free_squares.index(cpu)]
            cpusquares.append(cpu)
            moves[f"m{cpu}"] = "X"
            print(f"CPU guess: {cpu}")
            return


moves = {"m1": 1,
         "m2": 2,
         "m3": 3,
         "m4": 4,
         "m5": 5,
         "m6": 6,
         "m7": 7,
         "m8": 8,
         "m9": 9
}
free_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
usersquares = []
cpusquares = []


def main():
    # Game logic
    display_board()
    while free_squares:
        enter_move()
        display_board()
        if victory_for(usersquares):
            print("You win!")
            quit()

        if not free_squares:
            print("Tie!")

        draw_move()
        display_board()
        if victory_for(cpusquares):
            print("You lose!")
            quit()


if __name__ == "__main__":
    main()
