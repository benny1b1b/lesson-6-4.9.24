score: int = int(input("your score is: "))
if 0 <= score <= 40:
    print(" harder next time...")
elif 41 <= score <= 60:
    print("you're getting there, need some more work")
elif 61 <= score <= 80:
    print("good pretty")
elif 81 <= score <= 95:
    print("awesome!")
elif 96 <= score <= 100:
    print("excellent!!! You're a Star!")
else:
    print("grade illegal")
