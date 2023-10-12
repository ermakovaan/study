words = input().split()
ans = ''.join(word[-1] for word in words)
print(ans)
