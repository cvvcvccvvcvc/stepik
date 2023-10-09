word = input()
# d = {ch : num for _ in range(int(input())) for ch, num in [tuple(input().split(": "))]}
d = {}
for _ in range(int(input())):
    ch, num = input().split(": ")
    d[ch] = num
d2 = {ch : word.count(ch) for ch in word}
ans = {}

for k, v in d.items():
    for k2, v2 in d2.items():
        if int(v) == int(v2):
            ans[k2] = k
            continue
for ch in word:
    print(ans[ch], end="")

