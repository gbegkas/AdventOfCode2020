with open('Day2.txt', 'r') as fp:
    data = fp.read().splitlines()

passwords = [i.split(':') for i in data]
s = 0
for password in passwords:
    temp = password[0].split(' ')
    minmax = list(map(int, temp[0].split('-')))
    counter = password[1].count(temp[1])
    if counter > minmax[1] or counter < minmax[0]:
        s += 1
print(len(data) - s)

s = 0

for password in passwords:
    temp = password[0].split(' ')
    index = list(map(int, temp[0].split('-')))
    t = password[1][index[0]] + password[1][index[1]]
    if t.count(temp[1]) == 1:
        s += 1
print(s)
