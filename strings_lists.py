# 1 no
s = input("Enter a sentence: ")
print ("Reverse string: ",s[::-1])

# 2 no
s = input("Enter a sentence: ")

if(s[0::] == s[::-1]): # better way to check palindrome if s == s[::-1]:
    print("Palindrom")
else:
    print("Not palindrom")


# 3 no
scores = [88, 92, 79, 95, 60, 71]
scores.sort()
print("The lowest score: ",scores[0])
print("The highest score: ",scores[-1])
print("The average score: ",sum(scores)/len(scores))


# 4 no
s = input("Enter a sentence: ")
words = s.split()
count = len(words)
print("Number of words in the sentence: ",count)