class MultipleFunction():
    def Subfields():
            lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
            print("Sub-fields in AI are:")
            for item in lists:
                print(item)

    def OddEven():
        num=int(input("Enter a number:"))
        if num % 2 == 0:
            message=f"{num} is Even number"
        else:
            message=f"{num} is Odd number"
        return message

    def Elegible():
        gender=input("Enter your gender:").lower()
        age=int(input("Enter your age:"))
        print(f"Your Gender:{gender}")
        print(f"Your Age:{age}")
        if gender == "Male".lower() and age >= 21:
            message="ELIGIBLE"
        elif gender == "Female".lower() and age >= 18:
            message="ELIGIBLE"
        else:
            message="NOT ELIGIBLE"
        return message

    def percentage():
        sub1=98
        sub2=87
        sub3=95
        sub4=95
        sub5=93
        print(f"Subject1= {sub1}")
        print(f"Subject2= {sub2}")
        print(f"Subject3= {sub3}")
        print(f"Subject4= {sub4}")
        print(f"Subject5= {sub5}")
        total_marks = sub1+sub2+sub3+sub4+sub5
        percentage=total_marks/500 * 100
        return percentage

    def triangle():
        Height=32
        Breadth=34
        print(f"Height:{Height}")
        print(f"Breadth:{Breadth}")
        area = (Height*Breadth)/2
        print(f"Area of Triangle:{area}")
        Height1=2
        Height2=4
        Breadth=4
        print(f"Height1:{Height1}")
        print(f"Height2:{Height2}")
        print(f"Breadth:{Breadth}")
        perimeter=Height1+Height2+Breadth
        print(f"Perimeter of Triangle:{perimeter}")