

def get_full_name(name, surname, familyname=''):
    if familyname:
        return f"{name} {surname} {familyname}".title()
    else:
        return f"{name} {surname}".title()
    
print(get_full_name("dua", "lipa"))

