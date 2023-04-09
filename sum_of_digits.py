
'''nums = int(input("Enter some numbers: "))
result = 0
while nums != 0:
    digits = nums % 10
    result = result + digits
    nums = nums // 10
print(f"The sum of digits: {result}")
'''

nums = input("Enter some digits: ")

result = 0
for i in nums:
    result = result + int(i)
print(f"The sum of digits: {result}")
