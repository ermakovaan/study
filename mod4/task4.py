def palindrome(s):
    counter = {}
    single = ""
    result = ""
    for char in s:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
            if counter[char] == 2:
                counter[char] = 0
                result += char
    for char, counts in counter.items():
        if counts == 1:
            single = char
            break
    if len(result) > 1:
        return result + single + result[::-1]
    else:
        return f"Из слова {s} нельзя составить палиндром"

line = input("Введите слово: ")

if line == line[::-1]:
    print(f"Слово {line} является палиндромом")
else:
    print(palindrome(line))
