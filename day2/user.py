zdanie = input('Podaj jakies zdanie:')

# String wyjsciowy "Ala ma kota. "


zdanie = zdanie.strip()
print(zdanie)

zdanie = zdanie.capitalize()
print(zdanie)

zdanie += '.'
print(zdanie)

print(type(zdanie))
