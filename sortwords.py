with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]
for i in words:
    print(i)
words.sort()
for i in words:
    print(i)
with open('words.txt', 'w') as file:
    for item in words:
        file.write(f"{item}\n")