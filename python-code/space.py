


def user_info(name=None, surname=None, age=None, country=None, tel_number=None, email=None):
    user = {
            'name' : name,
            'surname' : surname,
            'age' : age,
            'country' : country,
            'tel_number' : tel_number,
            'email' : email }
    return user

print('Cv for users...')
users = []

while True:
    print('\nenter informations, \n', end='')
    name = input('enter your name : ')
    surname = input('enter your surname : ')
    age = input('enter your age : ')
    country = input('enter your country : ')
    tel_number = input('enter your telephone number : ')
    email = input('enter your email : ')

    users.append(user_info(name, surname, age, country, email=email))

    question = input("Do you want add any user? (yes or no) : ")
    if question.lower()== 'no':
        break
print("\n users in system : ")
for user in users:
    if tel_number and email:
        print(f" user information : \
            \nuser : {user['name'].title()} \
            \n age : {user['age']} \
            \n country : {user['country'].title()} \
            \n telephone number : {user['tel_number']} \
            \n email : {user['email']}")
    else:
        print(f" user information : \nuser : {user['name'].title()} \
            \n age : {user['age']} \
            \n country : {user['country'].title()}")


