def Simple_Calculator():
    while True:
        print("\nSimple Calculator")
        
        y = input("1.You want to proceed for calculation(Y/N)\n")
        if y == 'Y':
            
            a = int(input("Enter the value of a:\n"))
            print(input)
            b = int(input("Enter the value of b:\n"))
            c = input("Enter your operator:")
            print(input)
            match c:
                case'+':
                    print(a+b)
            match c:
                case'*':
                    print(a*b)
            match c:
                case'/':
                    print(a/b)
            match c:
                case'-':
                    print(a-b)
            match c:
                case'**':
                    print(a**b)
            match c:
                case'//':
                    print(a//b)
            match c:
                case'|':
                    print(a|b)
            match c:
                case'<<':
                    print(a<<b)
            match c:
                case'^':
                    print(a^b)
        elif y =="N":
                print("Visit us again!")
                break
        else:
            print("Invalid choice")
            break
            
Simple_Calculator()
