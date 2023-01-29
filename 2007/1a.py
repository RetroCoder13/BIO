import random
import math

print("Enter each number individually:")
numbers = [int(input()),int(input()),int(input()),int(input()),int(input())]
score = 0

def identicalNumbers(numbers):
    global score
    for i in range(10):
        if numbers.count(i+1) >= 2:
            score += int(math.factorial(numbers.count(i+1))/(math.factorial(2)*math.factorial(numbers.count(i+1)-2)))

def addToFifteen(numbers):
    global score
    for a in range(5):
        for b in range(4-a):
            b += a+1
            sum = numbers[a] + numbers[b]
            if sum == 15:
                score += 1
            for c in range(4-b):
                c += b+1
                sum = numbers[a] + numbers[b] + numbers[c]
                if sum == 15:
                    score += 1
                for d in range(4-c):
                    d += c+1
                    sum = numbers[a] + numbers[b] + numbers[c] + numbers[d]
                    if sum == 15:
                        score += 1
                    for e in range(4-d):
                        e += d+1
                        sum = numbers[a] + numbers[b] + numbers[c] + numbers[d] + numbers[e]
                        if sum == 15:
                            score += 1

identicalNumbers(numbers)
addToFifteen(numbers)
print("\nScore: ", score)