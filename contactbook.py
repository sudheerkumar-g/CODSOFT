contact={}
while True:
    choice=input("Enter your choice: \n 1. Add Contact \n 2. View contact list \n 3. Search Contact \n 4. Update Contact \n 5. Delete Contact \n 6. Exit ")
    if choice=='1':
        name=input("Enter Contact name: ")
        phone=input("Enter mobile number: ")
        mail=input("Enter email: ")
        address=input("Enter Address: ")
        contact[name]=phone,mail,address
    elif choice=='2':
        if not contact:
            print("contact book is empty")
        else:
            print(f"Name : {name} \n phone : {phone} \n Email : {mail} \n Address : {address}")
    elif choice=='3':
        search=input("Enter contact name: ")
        if search in contact:
            print(f"DETAILS: \n Name : {name} \n phone : {phone} \n Email : {mail} \n Address : {address}")
        else:
            print("Not found")
    elif choice=='4':
        edit=input("Enter name to edit: ")
        if edit in contact:
            phone=input("Enter mobile number: ")
            contact[edit]=phone
            print("Contact updated")
            print(f"Name : {name} \n phone : {phone} \n Email : {mail} \n Address : {address}")
        else:
            print("Not found")
    elif choice=='5':
        delc=input("Enter contact name: ")
        if delc in contact:
            contact.pop(delc)
            print("Contact deleted")
        else:
            print("Not found")
    else:
        break
