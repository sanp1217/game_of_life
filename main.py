import random


def dead_state(width, height):
    state = [[0 for i in range(width)] for j in range(height)]
    return state

def main():
    print((dead_state(2, 5)))

if __name__ == "__main__":
    main()