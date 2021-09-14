contacts = {
    'number':4,
    'students': [
        {'name': "Carston Work", 'email': 'bdrummerrr@gmail.com'},
        {'name': 'Harry Potter', 'email': 'harry@gmail.com'},
        {'name': "Hermione Granger", 'email': 'hermione@gmail.com'},
        {'name': 'Ronald Weasley', 'email': 'ron@gmail.com'}
    ]
}

for student in contacts['students']:
    print(student["email"])