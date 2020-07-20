num = input().split()
pos = 0
pos_count = 0
count = 0

for i in num:
    if int(i) < 0:
        count += 1
    else:
        pos += int(i)
        pos_count += 1

print(count)
print(round(pos / pos_count, 1) if pos else "0.0")