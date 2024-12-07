
num = 3
multiple = 1
mod = 13

while True:
    if ((num * multiple) % mod == 1):
        print(multiple)
        break
    multiple += 1