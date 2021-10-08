#starting on problem sovling 1

word = "Hello"
reversed_word = ''
word2 = "hello world"
capital_word = ''

for index in range(len(word) -1, -1, -1):
    reversed_word += word[index]

for index2 in range(0, len(word2) , 1):

    capital_word += word2[index2]

print(word)
print(reversed_word)
print(word2.upper())
print(capital_word)

