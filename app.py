weight = int(input('Enter Weight Please:'))
unit = input('(L)bs or (K)g:')
if unit.upper() == "L":
   converted = weight * 0.45
   print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} LBS")



