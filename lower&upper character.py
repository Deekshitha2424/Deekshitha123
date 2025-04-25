#Take input from the user
char=input("Enter singlecharacter.")
#check if the input is a single character
if len(char)!=1:
    print("please enter only one character!")
else:
    if char.isdigit():
        print(f"{char}'is a digit.")
        #check if the character is an lowercase letter
    elif char.islower(): 
        print(f"{char}'is a lowercase character.")
        #check if the character is an uppercase letter
    elif char.isupper():
        print(f"{char}' is an upper case character.")
        #If none of the above,it is a special character
    else:
        print(f"{char}' is a special character.")
        
