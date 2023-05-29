import random
import roman
import time

score = 0
start_time = time.time()

# Convert 10 random numbers from 1-2000 to roman numerals.
for i in range(10):
    random_number = random.randint(1, 2000)
    roman_number = roman.toRoman(random_number)
    correct = True

    # Ask for the Roman number and check if it is correct.
    # If not, ask again.
    while True:
        answer = input("What is the Roman number for %s ? " % random_number)
        if answer == roman_number:
            if correct:
                score += 1

            print("Correct 🎉")
            break
        else:
            correct = False
            print("Oops! Try again.")

elapsed_time = round(time.time() - start_time)
minutes, seconds = divmod(elapsed_time, 60)

if score == 10:
    print("\nAMAZING!!!")
elif score > 7:
    print("\nSuper!")
elif score > 4:
    print("\nWell done!")
print("\nYou scored %d points in %s minutes and %s seconds!" % (score, minutes, seconds))
