print("Learn Reverse Cipher ")

message = "Cyber-Nishanth"

translate = ""

# Find the message length --> returns no of char
#x  = len(message)

# Python Indexing value :
Len = len(message) -1

print(Len)

while Len >= 0:
    translate = translate + message[Len]
    Len = Len - 1

print(translate)

print("One line Reverse Ciper")
print(message[::-1])

Decrypt = str(input("Enter the txt to decrypt : "))
print(Decrypt[::-1])