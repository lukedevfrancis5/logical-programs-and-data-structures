credit_score = int(input("Enter your credit score: "))

if credit_score < 400 or credit_score > 850:
    print("Invalid Entry")

elif credit_score >= 400 and credit_score <= 600:
    print("Silver Card")

elif credit_score > 600 and credit_score <= 800:
    print("Gold Card")

elif credit_score > 800 and credit_score <=850:
    print("Platinum Card")