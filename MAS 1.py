import random
import time

print("Addition, Subtraction, and Multiplication; "
      "no paper, pens or calculators!")
response = input("Type 'y' of 'yes' to start ")
while response == "y" or response == "yes":
  MAS = random.randint(1, 3)
  if MAS == 1:
    num1 = random.randint(100, 999)
    num2 = random.randint(10, 99)
    print(num1, "+", num2)
    start = time.time()
    Q = int(input("= "))
    answer = num1 + num2
    if Q == answer:
      end = time.time()
      tim = end - start
      print("Correct!")
      if tim < 6:
        print("That was very quick!")
      elif tim < 9:
        print("That was fast")
      elif tim < 12:
        print("That was okay")
      elif tim < 15:
        print("That was slow")
      else:
        print("You must get faster!")
      print("It took you", round(tim, 2), "seconds")
    else:
      print("Incorrect! The answer was", answer)
  elif MAS == 2:
    num1 = random.randint(100, 999)
    num2 = random.randint(10, 99)
    print(num1, "-", num2)
    start = time.time()
    Q = int(input("= "))
    answer = num1 - num2
    if Q == answer:
      end = time.time()
      tim = end - start
      print("Correct!")
      if tim < 8:
        print("That was very quick!")
      elif tim < 12:
        print("That was fast")
      elif tim < 16:
        print("That was okay")
      elif tim < 20:
        print("That was slow")
      else:
        print("You must get faster!")
      print("It took you", round(tim, 2), "seconds")
    else:
      print("Incorrect! The answer was", answer)
  elif MAS == 3:
    num1 = random.randint(3, 12)
    num2 = random.randint(3, 12)
    print(num1, "*", num2)
    start = time.time()
    Q = int(input("= "))
    answer = num1 * num2
    if Q == answer:
      end = time.time()
      tim = end - start
      print("Correct!")
      if tim < 6:
        print("That was very quick!")
      elif tim < 9:
        print("That was fast")
      elif tim < 12:
        print("That was okay")
      elif tim < 15:
        print("That was slow")
      else:
        print("You must get faster!")
      print("It took you", round(tim, 2), "seconds")
    else:
      print("Incorrect! The answer was", answer)
  response = input("Do you want to test again? ")
print("See you next time")
