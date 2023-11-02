#!/usr/bin/python3
"""
Write a program that solves the N queens problem.
"""
import sys


def valid_pos(solution, pos):
    """
    Function that verifies if the position is valid
    """
    for queen in solution:
        if queen[1] == pos[1]:
            return False
        if (queen[0] + queen[1]) == (pos[0] + pos[1]):
            return False
        if (queen[0] - queen[1]) == (pos[0] - pos[1]):
            return False
    return True


def solve_queens(row, n, solution):
    """
    Function that finds the solution recursively, from the root down
    """
    if row == n:
        print(solution)
    else:
        for col in range(n):
            pos = [row, col]
            if valid_pos(solution, pos):
                solution.append(pos)
                solve_queens(row + 1, n, solution)
                solution.remove(pos)


def main():
    """ Validate the arguments from OS """
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        i = int(sys.argv[1])
    except BaseException:
        print('N must be a number')
        sys.exit(1)
    i = int(sys.argv[1])
    if i < 4:
        print('N must be at least 4')
        sys.exit(1)

    solution = []
    """ From root(0) down(n) """
    solve_queens(0, int(sys.argv[1]), solution)


if __name__ == '__main__':
    main()
