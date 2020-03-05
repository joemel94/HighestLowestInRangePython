def main():

    ct=int(input("Type Number of Inputs you need:"))
    i = 1
    a=[]
    while i <= ct:
        x=int(input("Enter an Integer:"))
        a.append(x)
        i += 1
    
    print("\n")
    print("\n")
    print(a)
    print("\n")
    print("Highest Value:",max(a))
    print("Lowest Value:",min(a))

    even=[]
    for y in range(0,len(a)):
        if y%2:
            even.append(a[y])

    Sum = sum(even)
    print("\n")
    print("Sum of Even Indices:",+Sum)
    print("\n")
    choice=input("Do you want to input another set of Numbers? type YES if you want to PROCEED And press ANY BUTTON to END   ").lower()
    if choice=="yes":
        main()
    else:
        exit()

main()
