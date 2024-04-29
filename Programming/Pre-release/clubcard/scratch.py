x = (2, 4, 6, 7, 8, 10)
for i in x:
    print(i)

count = 0
while x[count] % 2 == 0:
    print("found")
    count += 1
    