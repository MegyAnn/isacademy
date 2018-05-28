zdanie = input("Podaj zdanie : ")

if 'a' in zdanie:
    print("Jest mala literka a")

elif 'A' in zdanie:
    print('Jest duza litera A')
    if zdanie.count('A') > 2:
        print("Cos duzo tych literek A.")

elif 'x' in zdanie:
    print('Litera x w zdaniu')

else:
    print("Nic nie znalazlem")