def tower_of_hanoi(n):
    no_of_moves = 2 ** n - 1
    moves = []
    src = 'A'
    inter = 'B'
    dest = 'C'

    if n % 2 == 0:
        dest = 'B'
        inter = 'C'

    for i in range(1, no_of_moves + 1):
        if i % 3 == 1:
            moves.append(src + dest)
            print("Moving disc from ", src, "to", dest)
        if i % 3 == 2:
            moves.append(src + inter)
            print("Moving disc from ", src, "to", inter)
        if i % 3 == 0:
            moves.append(dest + inter)
            print("Moving disc from ", dest, "to", inter)

    return moves


print(tower_of_hanoi(4))