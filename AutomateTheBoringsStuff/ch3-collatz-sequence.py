def collatz(num):
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
    print(num)
    return num


try:
    inpt = int(input())
except Exception as e:
    print(e)

while inpt != 1:
    inpt = collatz(inpt)
