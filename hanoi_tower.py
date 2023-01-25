def hanoi_tower(n, fromPeg, toPeg):
    # this function should return a series of dublets
    # which represent the sequence of moves
    if n == 1:
        print(fromPeg, toPeg)
        return "Finished"
    unusedPeg = 6 - fromPeg - toPeg
    if n > 1:
        hanoi_tower(n - 1, fromPeg, unusedPeg)
        print(fromPeg, toPeg)
        hanoi_tower(n - 1, unusedPeg, toPeg)

hanoi_tower(3,1,3)

