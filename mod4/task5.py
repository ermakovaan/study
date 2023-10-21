def symbols(s):
    counts = {}
    for char in s:
        if char not in counts.values() and ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            counts.update({char: s.count(char)})
            return dict(sorted(counts.items(), key=lambda x: x[1]))

filename = input()
file = open(filename, 'r')
out = open("output5.txt", 'w')
stroke = file.read()
counts = symbols(stroke)
data = [f'{key}: {counts[key]}' for key in counts.keys()]
out.write('\n'.join(data))
out.close()
file.close()

