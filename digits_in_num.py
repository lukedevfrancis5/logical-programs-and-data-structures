
nums = int(input("Enter some numbers: "))

while nums != 0:
    digits = nums % 10
    print(f"{digits}", end=" ")
    nums = nums // 10
    