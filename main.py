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


# Takes the coordinates of the current cell and the board
# state as parameters and returns how many neighbors are around that cell.
def get_cell_live_neighbors(cell_coord, board_state):
    live_neighbors = 0
    height = len(board_state)
    width = len(board_state[0])
    x = cell_coord[0]
    y = cell_coord[1]

    for i in range((x - 1), (x + 2)):
        #to not go off the edge of board
        if i < 0 or i >= width: continue

        for j in range((y - 1), (y + 2)):
            #to not go off edge of board
            if j < 0 or j >= height: continue

            #So the current cell is not counted as a neighbor
            if i == x and j == y: continue

            if board_state[i][j] == 1:
                live_neighbors += 1

    return live_neighbors


def get_cell_state(live_neighbors, curr_cell_state):
    if curr_cell_state == 1:
        if live_neighbors <= 1 or live_neighbors > 3:
            return 0
        else:
            return 1

    elif curr_cell_state == 0:
        if live_neighbors == 3:
            return 1
        else:
            return 0


def next_board_state(initial_state):
    new_state = random_state(len(initial_state[0]), len(initial_state))
    live_neighbors = 0

    for i in range(len(initial_state)):

        for j in range(len(initial_state[0])):
            live_neighbors = get_cell_live_neighbors((i, j), initial_state)
            new_state[i][j] = get_cell_state(live_neighbors, initial_state[i][j])

    return new_state


def main():
    board = random_state(3, 3)
    for i in board:
        print(*i)
    # render(board)
    
    new_board = next_board_state(board)

    print()
    for j in new_board:
        print(*j)

if __name__ == "__main__":
    main()
