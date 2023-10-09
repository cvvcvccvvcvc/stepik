# put your python code here
d = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    if name in d:
        d[name].append(phone)
    else:
        d[name] = [phone]

for _ in range(int(input())):
    print(*d.get(input().lower(), ["абонент не найден"]))