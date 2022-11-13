# Right triangle pattern of star
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

# Inverted right triangle star pattern:
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")

    print("\n")

# Right triangle pattern of alphabets:
rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("\n")

# Inverted Right triangle pattern of alphabets:
rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows, 0, -1):
    for j in range(0, i):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("\n")


