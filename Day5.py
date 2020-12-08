with open('Day5.txt', 'r') as fp:
    bpasses = fp.read().splitlines()
passes = []
sId = []
for bpass in bpasses:
    row = bpass[:-3]
    col = bpass[7:]
    row = row.replace('F', '0')
    row = row.replace('B', '1')
    col = col.replace('L', '0')
    col = col.replace('R', '1')
    sId.append(int(row, 2) * 8 + int(col, 2))
maxId = max(sId)
minId = min(sId)
sumId = sum(sId)
s = sum(i for i in range(minId, maxId +1))
print(s - sumId)
pass