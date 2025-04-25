#Python program toprint the Fibonacci sequence using while loop
#Number of terms to display
n_terms=int(input("Enter the number of Fibonacci terms to dispaly:"))
#First two terms
a,b=0,1
count=0
#check if the number of terms is valid
if n_terms<=0:
    print("please enter a postive integer.")
elif n_terms==1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count<n_terms:
        print(a,end="")
              #update values
        a,b=b,a+b
        count+=1
