# both programs output a reversed version of input

'''nums = int(input("Enter some numbers: "))

while nums != 0:
    digits = nums % 10
    print(f"{digits}", end=" ")
    nums = nums // 10

'''

nums = input("Enter some numbers: ")
for digit in nums[::-1]:
    print(f"{digit}", end=" ") 
    