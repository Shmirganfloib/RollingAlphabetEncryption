user_input = input("Enter text: ")
user_input = user_input.lower()
total = 0
for i in range(len(user_input)):
    n = ord(user_input[i]) - 96
    total += (26 ** i) * n
print("Encrypted text: " + str(total))
