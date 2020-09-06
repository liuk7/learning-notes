# while True:
#     try:
n, nums = int(input()), map(int, input().split())
pos = []
neg = 0

for e in nums:
    if e < 0:
        neg += 1
    elif e >= 0:
        pos.append(e)

pos_e = sum(pos) / len(pos)

print(str(neg) + ' ' + str(round(pos_e, 1)))


    # except:
    #     break