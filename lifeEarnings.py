#Lifetime Earnings
#Tyler Hegewald

name = input("Please enter your name ")
age = int(input("Please enter your age "))
salary = int(input("Please enter your salary "))



for x in range(67-age):
    if age < 67:
        raises = salary * .04
        salary = salary + raises
        salary = float(salary)
print(name,"will earn about","$%.2f"%salary)


