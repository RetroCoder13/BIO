word = input("Word: ")
digitWords = ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
currentWord = [0,0,0,0,0,0,0,0,0]

for index,letter in enumerate(word):
    for indexWord,word in enumerate(digitWords):
        if letter == word[currentWord[indexWord]]:
            currentWord[indexWord] += 1
            if currentWord[indexWord] == len(digitWords[indexWord]):
                print(indexWord+1)
                exit()

print("NO")