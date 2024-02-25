class SubfieldsInAI():
    def Subfields():
        subdomain=["Machine Learning","Neural Networks","Vision,Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for temp in subdomain:
            print(temp)
        return      


class OddEven():
    def OddEven():
        num=int(input("Enter a number:"))
        if (num%2)==0:
            print (num,"is Even number")
        else:
            print (num,"is Odd number")
        return
    
class ElegiblityForMarriage():
    def Elegible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if (Gender=="Male" and Age>21):
            print ("Eligible")
        elif (Gender=="Female" and Age>18):
            print ("Eligible")
        else:
            print ("Not Eligible")
        return
    
class FindPercent():
    def percentage():
        subject1=int(input("Subject1="))
        subject2=int(input("Subject2="))
        subject3=int(input("Subject3="))
        subject4=int(input("Subject4="))
        subject5=int(input("Subject5="))
        Total=subject1+subject2+subject3+subject4+subject5
        Percentage = Total/5
        print("Total :",Total)
        print("Percentage :",Percentage)
        return
    
class triangle():
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print ("Area formula: (Height*Breadth)/2")
        Area=(Height*Breadth)/2
        print("Area of Triangle:",Area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print ("Perimeter formula: Height1+Height2+Breadth")
        Perimeter=Height1+Height2+Breadth
        print ("Perimeter of Triangle:",Perimeter)
        return
    
    