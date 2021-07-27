import addition, division, multiplication, subtraction

print("Welcome to the simple calculator, please select from the following options: ")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")


selection = input("Please enter your selection: ")
num_one = int(input("Please enter number one: "))
num_two = int(input("Please enter number two: "))


if(selection == "1"):
    # python does not recognize string + number(make int into string)
   print("Your result is: " + str(addition.add(num_one, num_two)))
elif(selection == "2"):
    print("Your result is: " + str(subtraction.sub(num_one, num_two)))
elif(selection == "3"):
    print("Your result is: " + str(multiplication.mul(num_one, num_two)))
elif(selection == "4"):
    print("Your result is: " + str(division.div(num_one, num_two)))
else:
    print("Invalid entry!")

