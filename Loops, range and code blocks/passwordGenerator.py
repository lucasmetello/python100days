import random
print("Welcome to the PyPassword Generator!")

size = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols = ["!","@","#","$","%","&","*"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

password = [""] * size
print(password)

for a in range(0, size):# "a" is a counter that counts to "size" size
    position = random.randint(0, len(letters))# "position" receive a random value between 0 and "letters" size
    password[a] = letters[position]

for b in range(0, symbol):# "b" is a counter that counts to "symbol" size
    position = random.randint(0, len(symbols))# "position" receive a random value between 0 and "symbols" size
    password[a] = symbols[position]

for c in range(0, num):# "a" is a counter that counts to "num" size
    position = random.randint(0, len(numbers))# "position" receive a random value between 0 and "numbers" size
    password[a] = numbers[position]


print("Here is your password is: ", str(password)[1:-1])
