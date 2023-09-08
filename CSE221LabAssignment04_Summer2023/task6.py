def DFS_FloodFill(r, c, rows, cols, G):
    if r < 0 or r >= rows or c < 0 or c >= cols or G[r][c] == '#':
        return 0

    count = 0
    if G[r][c] == 'D':
        count += 1

    G[r][c] = '#'

    count += DFS_FloodFill(r + 1, c, rows, cols, G)
    count += DFS_FloodFill(r - 1, c, rows, cols, G)
    count += DFS_FloodFill(r, c + 1, rows, cols, G)
    count += DFS_FloodFill(r, c - 1, rows, cols, G)

    return count

def countdiamonds(rows, cols, G):
    maxDiamonds = 0
    for r in range(rows):
        for c in range(cols):
            if G[r][c] == '.':
                diamond = DFS_FloodFill(r, c, rows, cols, G)
                maxDiamonds = max(maxDiamonds, diamond)
    return maxDiamonds


f1 = open("input6_3.txt", "r")
f2 = open("output6_3.txt", "w")
lines = f1.read().split("\n")
R, H = map(int, lines[0].split())

G = [list(line) for line in lines[1:]]

result = countdiamonds(R, H, G)

f2.write(str(result))
f2.close()