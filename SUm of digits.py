# Sum of Digits

sum_of_each_line = []
lines =raw_input()
print(type(lines))

for i in range(int(lines)):
    msg = input()
    sum = 0
    for x in msg:
        sum+=int(x)
    sum_of_each_line.append(sum)

[print(x) for x in sum_of_each_line]


