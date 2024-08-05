separator = "\u2400" #this because user has freedom to choose every nick



def sign_in():
    check = 0
    while check == 0 :
        username = input("Username: ")
        with open("accounts.txt","r") as f :
            for line in f.readlines():
                userNames , passWords = line.strip().split(separator)
                while username == userNames :
                    check += 1
                    password = input("Enter your password: ")
                    if password == passWords :
                        print("Welcome!!",username,)
                        break
                    else :
                        print("Wrong Password. Try Again")
               
      
        if check == 0 :
            print("This username is nonexist. Try again")
        

               
        



def sign_up():
    username = input("Enter your username: ")
    with open("accounts.txt","r") as f :
        for line in f.readlines():
            userNames , passWords = line.strip().split(separator)
            while username == userNames :
                print("This username has been used. Select another.")
                username = input("Enter your username: ")
                
    with open("accounts.txt","a+") as f :
        f.write(username + separator)        

    password = input("Enter your password: ")
    with open("accounts.txt","a") as f :
        f.write(password + "\n")
        
    


                





while True :
    choice = input("Press 1 to Sign In , Press 2 to Sign Up: ")
    if choice == "1" :
        sign_in()
        break
    elif choice == "2" :
        sign_up()
        break
    else :
        print("Invalid Choice")
        continue

    