import random


def random_state(width, height):
    state = []

    for i in range(height):
        temp = []
        for j in range(width):
            random_num = random.random()
            if random_num >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            temp.append(cell_state)
        state.append(temp)

    return state


def render(board_state):
    for i in range(len(board_state)):
        print("")

        # % is symbol for alive, . is for dead cell.
        for j in range(len(board_state[0])):
            if board_state[i][j] == 1:
                print('%', end=" ")
            else:
                print('.', end=" ")


def next_board_state(board_state):
    return 0


def main():
    board = random_state(20, 30)
    print(board)
    render(board)


if __name__ == "__main__":
    main()