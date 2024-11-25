book = {}

def add_contact(name, phone, email):
    if name in book:
        book[name]['phone'].append(phone)
        book[name]['email'].append(email)
    else:
        book[name] = {'phone': [phone], 'email': [email]}

def search_contact(name):
    contact = book.get(name)
    if contact:
        print(f"contact found: {name}")
        print(f"phone: {contact['phone']}")
        print(f"email: {contact['email']}")
    else:
        print(f"no contact found with the name {name}.")

def remove_contact(name):
    if name in book:
        del book[name]
        print(f"contact '{name}' has been removed.")
    else:
        print(f"contact '{name}' not found.")
    
def main():
    while True:
        print("\ncontact book option:")
        print("1. add contact")
        print("2. search contact")
        print("3. remove contact")
        print("4. exit") 
        choice = input("choose an option (1/2/3/4):")

        if choice == '1':
            name = input("enter name: ")
            phone = input("enter phone: ")
            email = input("enter email: ")
            add_contact(name, phone, email)
            print("contact added.")
        
        elif choice == '2':
            name = input("enter name to search: ")
            search_contact(name)

        elif choice == '3':
            name = input("enter name to remove: ")
            remove_contact(name)

        elif choice == '4':
            print("exiting contact book app.")
            break

        else:
            print("invalid choice. please try again.")

if __name__ == "__main__":
    main()




 
