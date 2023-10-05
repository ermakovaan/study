words = input('Введите слова (через пробел): ')
string = ''
for i in range(len(words)):
    if words[i] == ' ':
        string += words[i-1]
    if i == len(words) - 1:
        string += words[i]
print(string)