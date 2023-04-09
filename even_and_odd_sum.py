nums = int(input("Enter some numbers: "))
even_sum = 0
odd_sum = 0
while nums != 0:
    digits = nums % 10
    if digits % 2 == 0:
        even_sum+= digits
    else:
        odd_sum += digits
    nums = nums // 10
print(f"The sum of even digits: {even_sum}")
print(f"The sum of odd digits: {odd_sum}")
