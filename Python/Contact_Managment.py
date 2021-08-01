import pickle
print("\t\tWelcome to Address Book\n1. Add_contact\n2. Display_contact\n3. Delete_contact\n4. Modify_contact\n5. Search_contact")
choice = input("\nEnter your choice: ")
print("\nEnter 0 to exit")

def pickle_write():
    with open('contacts.pickle.txt', 'wb') as file:
        pickle.dump(list_contacts, file, protocol=pickle.HIGHEST_PROTOCOL)


def pickle_get():
    with open('contacts.pickle.txt', 'rb') as file:
        try:
            list = pickle.load(file)
        except EOFError:
            list = []
        return list
list_contacts = pickle_get()
if not list_contacts:
    pickle_write()
while choice:
    if choice == "1":
        name = input("Enter contact name: ")
        email = input("Enter contact email: ")
        phone = input("Enter contact number: ")
        contact_details = {"name": name, "email": email, "phone": phone}
        list_contacts.append(contact_details)
        pickle_write()
        print("\nContact successfully added")

    elif choice == "2":
        list_contacts = pickle_get()
        if list_contacts:
            for i in list_contacts:
                print(
                    f"\nName: {i['name']}\nEmail: {i['email']}\nContact Number: {i['phone']}")
        else:
            print("No such contact in address book")

    elif choice == "3":
        list_contacts = pickle_get()
        if not list_contacts:
            print("Address book empty. No contact to delete")
        else:
            name = input("Enter contact name: ")
            for i in list_contacts:
                if i["name"] == name:
                    list_contacts.remove(i)
                    print("Contact Successfully Deleted")
                    pickle_write()
                    break
            else:
                print("No contact with this name")

    elif choice == "4":
        list_contacts = pickle_get()
        if not list_contacts:
            print("Address book empty. No contact to modify")
        else:
            name = input("Enter contact name: ")
            for i in range(len(list_contacts)):
                if list_contacts[i]["name"] == name:
                    name = input("Enter new name: ")
                    email = input("Enter new email: ")
                    phone = input("Enter new number: ")
                    contact_details = {"name": name,
                                    "email": email, "phone": phone}
                    list_contacts[i] = contact_details
                    print("\nContact modified")
                    pickle_write()
                    break
            else:
                print("No contact with this name found")

    elif choice == "5":
        list_contacts = pickle_get()
        if not list_contacts:
            print("Address book empty. No contact to delete")
        else:
            name = input("Enter contact name: ")
            for i in list_contacts:
                if i["name"] == name:
                    print("Email:", i["email"])
                    print("Contact Number:", i["phone"])
                    break
            else:
                print("No contact with this name found")
    elif choice == "0":
        print("\n\nThanks for logging in :)")
        break
    else:
        print("Invalid Choice!!!")
    choice = input("\nEnter your choice: ")