import random
import os
class Employee():
    def __init__(self,name,salary=0):
        self.name=name
        self.__emp_id=random.randint(1000,9999)
        self.__salary=salary
    
    def update_salary(self,new_salary):
        try:
            if new_salary<0:
                raise ValueError("ERROR!!!!.... Enter amount in positve form")
            self.__salary=new_salary
            print("Salary Updated Successfully-----")
        except ValueError as e:
            print(e)
    def show_details(self):
            print(f"Employee ID: {self.__emp_id} \nName: {self.name} \nSalary: {self.__salary}")

    def save_data(self):
         try: 
            with open("employee.txt","a") as file:
                file.write(f"Employee ID: {self.__emp_id} \nName: {self.name} \nSalary: {self.__salary}")
                print("Data Save Successfully!!!!-----")
         except FileNotFoundError:
            print("File not found")
    def get_salary(self):
            return self.__salary 
    def calculate_pay(self):
            pass
    
class FullTimeEmployee(Employee):
        def __init__(self,name,salary=0, bonus=0):
            super().__init__(name,salary)
            self.bonus=bonus
        def calculate_pay(self):
            total=super().get_salary()+self.bonus
            print(f"Total monthly salary: {total}")
        
   
class PartTimeEmployee(Employee):
        def __init__(self, name, hourly_rate, hours_worked):
           self.hours_worked = hours_worked
           self.hourly_rate=hourly_rate
           salary=hourly_rate*hours_worked
           super().__init__(name,salary)
        def calculate_pay(self):
           total= self.hourly_rate+self.hours_worked
           print(f"Total pay for part-time:{total}")

def load_employees_data():
    print("Loading saved data........")
    if os.path.exists("employee.txt"):
        with open("employee.txt","r") as file:
            data=file.readlines()
            if not data:
                print("No details saved.......")
            for i in data:
                print(i)
               
print("*****EMPLOYEE PAYROLL MANAGEMENT SYSTEM*****")
load_employees_data()
try:
    name= input("Enter Employee Name: ")
    print("Choose Employee Type: ")
    print("1. Full-Time Employee")
    print("2.Part-Time Employee")
    choice= int(input("Enter your Choice: "))

    if choice==1:
        salary=float(input("Enter Monthly salary: "))
        bonus= float(input("enter bonus amount: "))
        emp =FullTimeEmployee(name,salary,bonus)
    elif choice==2:
        hourly_rate=float(input("enter hourly rate: "))
        hours_worked= float(input("enter total hours worked: "))
        emp =PartTimeEmployee(name,hourly_rate,hours_worked)
    else:
        raise ValueError("Invalid Choice!")
    
    while True:
        print("\n--------- MENU ---------")
        print("1. Update Salary")
        print("2. Calculate Pay")
        print("3. Show Employee Details")
        print("4. Save & Exit")

        option = int(input("Enter Your Choice (1-4): "))
        if option == 1:
            try:
                new_salary = float(input("Enter New Salary: "))
                emp.update_salary(new_salary)
            except ValueError:
                print("Enter a valid salary amount: ")
        elif option == 2:
            emp.calculate_pay()
        elif option == 3:
            emp.show_details()
        elif option == 4:
            emp.save_data()
            print("Employee data saved successfully!")
            break
        else:
            print("Invalid Option! Please choose 1-4.")

except ValueError as e:
    print("ERROR!!!", e)
except Exception as e:
    print("Unexpected Error!!!", e)


