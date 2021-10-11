#starting on problem sovling 1

word = "Hello"
reversed_word = ''
word2 = "hello world"
how_many = "aaaabbbbcccdddd"

for index in range(len(word) -1, -1, -1):
    reversed_word += word[index]


print(reversed_word)

first_letter_capital = word2.title()

print(first_letter_capital)

def compress_string(string):
    string_value = ""
    count = 1
    string_value += string[0]
    for letter in range(len(string)-1):
        if(string[letter] == string[letter+1]):
            count+=1
        else:
            if(count > 1):
                string_value += str(count)
            string_value += string[letter+1]
            count = 1
    if(count > 1):
        string_value += str(count)
    return string_value

print(compress_string(how_many))
print(compress_string("happy"))



