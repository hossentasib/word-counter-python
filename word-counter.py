# Read File and Customize
with open("text.txt", mode="r") as file:
    wordsall = []
    for line in file.readlines():
        words = line.strip().split(" ")
        wordsall += words
    
print(len(wordsall))