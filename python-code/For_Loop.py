
# lesson 9

from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA


guests = ['djohn', 'jack', 'potter', 'dua']
for guest in guests:
    print("Hi", guest.title())
    print("bye", guest.title())
    
    guests = ['djohn', 'jack', 'potter', 'dua']
for guest in guests:
    print("Hello", guest.title(), ", we are invite you our home")
    print("Will you come", guest.title(), " ?")
    print(f"Dear {guest.title()}, I think, it`s impossible\n")
    print(f"Thank you for calling, {guest.title()}.\n")
    
numbers = list(range(0, 13))
for number in numbers:
    print(f"The square of the number is {number**2}")
    
numbers = list(range(11))
square_numbers = []
for number in numbers:
    square_numbers.append(number**2)

print(numbers)    
print(square_numbers)    

friends = []
print("Enter your 5 closest friends")
for n in range(5):
    friends.append(input(f"{n+1} - enter your friend\n >> "))
    print("List of your friends", friends)

# Homework

names = ['alex', 'martin', 'melmon', 'gloria']
for name in names:
    print(f"hello {name}, how are you?")
print(f"code repeated ", {len(name)})

odd_numbers = list(range(11, 100, 2))
for odd_number in odd_numbers:
    print(odd_number**3)

films = []
print("Enter your favorite movies")
for film in range(5):
    films.append(input(f"{film+1} - enter favourite films\n >> "))
    
print(f"List of your favourite films {films}")

How_people = int(input("How many people do you conversation today?\n >> "))
people = []
for n in range(How_people):
    people.append(input(f"{n+1} - suhbat qilgan odamingiz kim edi?\n >> "))
    print(f"You have interviewed", {len(people)}, "people", people)
    