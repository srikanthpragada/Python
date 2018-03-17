# program to create a dictionary with name and mobile numbers

phones = {}
while True:
    name = input("Enter name :")
    if name == "end":
        break

    mobile = input("Enter mobile number :")

    if name in phones:  # name is found
        phones[name].add(mobile)   # add new number to existing set
    else:
        phones[name] = {mobile}   # Add a new entry with name and set

# print directory

for name, numbers in phones.items():
    print(name, numbers)


Sample Run
==========
Enter name :a
Enter mobile number :434343
Enter name :b
Enter mobile number :343434343
Enter name :a
Enter mobile number :23232
Enter name :b
Enter mobile number :23232232
Enter name :c
Enter mobile number :343434
Enter name :end
a {'23232', '434343'}
b {'343434343', '23232232'}
c {'343434'}
