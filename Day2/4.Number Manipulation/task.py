bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))
print(round(bmi))
print(round(bmi, 1))


score = 0

# User scores a point

score += 1 # -> score = score + 1
print(score)

# f-Strings
print("Your score is " + str(score))
print("Your score is %d" %(score))
print("Your score is {}" .format(score))
print(f"Your score is {score}")


score = 0
height = 1.8
is_winning = True

print(f"Your score is: {score}, your height is: {height}. Your winning is: {is_winning}")

