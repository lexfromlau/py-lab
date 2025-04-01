username = input('Enter your first name: ')
favorite_color = input('What\'s your favorite color? ')
birth_year = input('Birth year: ')
age = 2025 - int(birth_year)

print(f"{username.capitalize()}\'s favorite color is {favorite_color.lower()}. {username.capitalize()} is {age} years old.")