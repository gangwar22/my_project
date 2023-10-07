import json

mydict = {}

while True:
    print("1. Create\n2. Update\n3. Read\n4. Delete\n5. Exit") 
    choose = input("Enter the option--->>:")

    if choose == "1":
        print("Welcome to create")
        name = input("Enter the name->:")
        email = input("Enter the email address---->>:")
        while not email or "@" not in email or "." not in email:
            print("Please enter a valid email address")
            email = input("Enter the email address---->>:")
        number = input("Enter the number---->>:")
        while not number.isdigit() or len(number) != 10:
            print("Please enter a valid 10-digit number")
            number = input("Enter the number---->>:")
        password = input("Enter your password: ")
        while not (any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and len(password) >= 8):
            print("Please enter a strong password.")
            password = input("Enter your password: ")
        print("sucessfully created")
        mydict.update({number: {"name": name, "email": email, "number": number, "password": password}})
        with open("con.json", "w") as f:
            json.dump(mydict, f)# Write mydict as a JSON object into the file


    elif choose == "2":
        phone = input("Enter phone number: ")
        if phone in mydict:
            print("1. Update name\n2. Update email\n3. Update password")
            select = input("Enter the option you want to select-->>>: ")
            if select == "1":
                new_name = input("Enter new name: ")
                mydict[phone]["name"] = new_name
            elif select == "2":
                new_email = input("Enter new email address---->>:")
                while not new_email or "@" not in new_email or "." not in new_email:
                    print("Please enter a valid email address")
                    new_email = input("Enter new email address---->>:")
                mydict[phone]["email"] = new_email
            elif select == "3":
                new_password = input("Enter new password: ")
                while not (any(char.islower() for char in new_password) and any(char.isupper() for char in new_password) and any(char.isdigit() for char in new_password) and len(new_password) >= 8):
                    print("Please enter a strong password.")
                    new_password = input("Enter new password: ")
                mydict[phone]["password"] = new_password
            with open("con.json", "w") as f:
                print(json.dump(mydict,f,indent=5))
        else:
            print("Phone number not found.")

    elif choose == "3":
        phone = input("Enter the number--->>:")
        with open("con.json", "r") as f:
            x=json.load(f)
            if phone in x:
                    print(x[phone])
            else:
                print(f"The number {phone} does not exist in the dictionary.")
                print("\n")

    elif choose == "4":
        phone = input("Enter phone number: ")
        with open("con.json", "r") as f:
            y=json.load(f)
            if phone in y:
                print("1. Delete name\n2. Delete Email\n3. Delete password")
                select1 = input("Enter the option to select-->>>: ")
                if select1 == "1":
                    del y[phone]["name"]
                elif select1 == "2":
                    del y[phone]["email"]
                elif select1 == "3":
                    del y[phone]["password"]
                else:
                    print("sucessfully deleted")
                with open("con.json", "w") as f:
                    json.dump(y, f,indent=5)

            else:
                print("Phone number not found.")

    elif choose == "5":
        print("Exiting the program.")
        with open("contants.json", "w") as json_file:
            json.dump(mydict, json_file, indent=5)
        break
    else:
        print("Invalid option. Please choose a valid option (1-5).")

    print("\n")
    


