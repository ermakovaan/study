phone_number = input()
ans = (phone_number.
       replace('-', '').
       replace(')', '').
       replace('(', '').
       replace(' ', '')
       )
print(ans)
