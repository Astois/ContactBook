def main():
    while True:
        contactbook = input("do you want to continue to the contact book?.. ")
        if contactbook.lower() == "yes":
            Action = input("View, Delete, Add? ")
            if Action == "add":
                def add():
                    BookInput = input("Please enter a contact to add... ") # get user input

                    # open the file in append mode
                    with open ("ContactBook.txt", "a") as f:
                        f.write(BookInput + '\n')  # write to the file
                        print("Added!")   # display message
                add()        
            if Action == "view":
                def  view():
                    with open ("ContactBook.txt", "r") as f:
                        lines = f.readlines() # read all lines from the file
                        FirstWords = [lines.strip().split()[0] for lines in lines ]   # split each line into words and take first word only
                        print(FirstWords)
                        ViewL = input("what contact do you want to View?.. ")
                        for line in lines:   # iterate over each line
                            if ViewL in line:     # check if the word is present in the line
                                SLine = line.strip().split()   # remove leading and trailing spaces
                                print(SLine)     # print only the second element of split string
                view()            
            if Action == "delete":
                def delete():
                    with open ( "ContactBook.txt", "r+") as f:  # Open the file in 'read & write' mode
                        Lines = f.readlines()
                        FirstWords = [line.split()[0] for line in Lines]   # Get first words from each line
                        print(FirstWords)
                        DelLine = input("What Contact Do You Want To Delete?.. ")
                        f.seek(0)
                        for line in Lines:
                            if DelLine not in line:
                                f.write(line)   # Write remaining lines back to the file
                        f.truncate()
                        print("Deleted!")        # display message
                delete()  
        elif contactbook.lower() == "no":
            print("Exiting...")
            break          
main()