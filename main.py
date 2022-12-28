import random

def random_state(width, height):
    state = []

    for i in range(height):
        temp = []
        for i in range(width):
            random_num = random.random();
            if random_num >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            temp.append(cell_state)
        state.append(temp)

    return state


def main():
    print((random_state(2, 5)))

if __name__ == "__main__":
    main()