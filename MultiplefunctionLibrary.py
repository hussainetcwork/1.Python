class multiplefuctions():
    def AgeCategory():
        age=int(input("Enter the Age:"))
        if (age<18):
            category="Child"
        elif(age<39):
            category="Adult"
        elif(age<59):
            category="Citizen"
        else:
            category="Senior Citizen"
        return category
    
    def addition ():
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        add=num1+num2
        return add