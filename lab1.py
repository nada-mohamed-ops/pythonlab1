# Q1
amount = 47.28
tip_persent = 0.15
total_amount = (amount * tip_persent)+amount
amount_per_person = total_amount / 2
print(f'Each person needs to pay:{amount_per_person}')


# Q2
num1=input("enter number1 : ")
num2=input("enter number2 : ")

if not (num1.isdigit() and num2.isdigit()):
    print('invalid number')
else:
    if num2 == 0:
        print("cannot divide by zero.")
    else:
        result = int(num1 )/ int(num2)
        print(f'the result of {num1}  {num2} = {result}')




# Q3

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "{}"
word6 = "so"
word7 = "far?"

print(f"{word5[0]} {word1} {word2} {word3} {word4} {word6} {word7} {word5[1]}")




# Q4


word5 = "{}"
word7 = "far?"

new_word7 = word7.replace("?", f"!")
print(new_word7)
word5 = "{}"
new_word5 = word5.format("i love python")
print(new_word5)


# Q5


statement = len(input("Enter a statement: "))
print(f"The statement has ({statement}) characters.")




# Q6




num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))

print("Select operation:- ")
print("1- Add")
print("2- Subtract")
print("3- Multiply")
print("4- Divide")

choice = input("Enter choice (1/2/3/4):- ")

if choice == "1":
    print(f"Result: {num1 + num2}")
elif choice == "2":
    print(f"Result: {num1 - num2}")
elif choice == "3":
    print(f"Result: {num1 * num2}")
elif choice == "4":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input")


