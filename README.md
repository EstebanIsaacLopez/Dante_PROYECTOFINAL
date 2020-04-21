# Dante_PROYECTOFINAL
# Dante's Final Project DB

import sqlite3
from ClassLib import Employee as emp
from ClassLib import Department as  dpto
from ClassLib import PaymentHistory as paym

#Connection
conn = sqlite3.connect('Stephany5.db')  
c = conn.cursor() 
#Enabling foreign keys
conn.execute("PRAGMA foreign_keys = 1")

#script for creation of tables
c.execute("""CREATE TABLE IF NOT EXISTS  Employee (
            employee_id integer UNIQUE, 
            first text,
            last text,
            job text,
            pay real,
            department_ Text,
            foreign key (department_) REFERENCES Department(department_id)

            )""")

c.execute("""CREATE TABLE IF NOT EXISTS  Department (
            department_id Text UNIQUE, 
            budget real,
            phone integer)
          """)

c.execute("""CREATE TABLE IF NOT EXISTS  PaymentHistory (
            pk INTEGER PRIMARY KEY AUTOINCREMENT , 
            employee integer,
            NetPay real,
            PaymentDate Text,
            foreign key (employee) REFERENCES Employee (employee_id)
        
            )""")

conn.commit()

#Code for insertions
def insert_emp(emp):
    params= (emp.employee_id, emp.first, emp.last, emp.job, emp.pay, emp.dpto)
    with conn:
        c.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?)", params)

def insert_dpto(dpto):
    params=(dpto.name, dpto.budget, dpto.phone)
    with conn:
        c.execute("INSERT INTO Department VALUES (?, ?, ?)", params)

def insert_pay(pay):
    with conn:
        c.execute("INSERT INTO PaymentHistory VALUES (:pk, :empl, :netpay, :date)", {'pk':None, 'empl': pay.employee, 'netpay': pay.netpay, 'date': pay.dates})

#Code for searches
def get_emps_by_name(x):
    c.execute("SELECT * FROM Employee WHERE employee_id=:id", {'id': x})
    return c.fetchall()

def get_dpto_by_name(x):
    c.execute("SELECT * FROM Department WHERE department_id=:phon", {'phon': x})
    return c.fetchall()

def get_pay_by_name(x):
    c.execute("SELECT * FROM PaymentHistory WHERE employee=:emp", {'emp': x})
    return c.fetchall()

#Code for updates
def update_dpto (x, y):
    with conn:
        c.execute("UPDATE Department SET budget=:bud WHERE department_id=:nam", {'bud':y, 'nam':x })

def update_emp (x, y):
    with conn:
        c.execute("UPDATE Employee SET pay=:bud WHERE employee_id=:nam", {'bud':y, 'nam':x })

#Code for deletions
def remove_emp(x):
    with conn:
        c.execute("DELETE from Employee WHERE employee_id= :idd", {'idd': x} )
def remove_dpto(x):
    with conn:
        c.execute("DELETE from Department WHERE department_id= :idd", {'idd': x} )

#Code for console application
def App_UI():
    T=True;
    while T==True:
        print("\nBusiness School New Generation")  
        print("      Dante (2020)    \n")
        print("Choose an option :")
        print("1. New record ")
        print("2. Update record ")
        print("3. Delete record")
        print("4. Display record")
        print("5. Exit application")
        ans= int(input());

        if ans==1:
            print("Choose an option: ")
            print("1. New Employee ")
            print("2. New Department ")
            print("3. New Payment")
            an1= int(input())
            if an1==1:
                print ("Please provide data : Employee ID- First Name- Last Name- Job Title- Gross Salary- Department ")
                employee_id= int (input())
                first=input()
                last=input()
                job=input()
                salary=float(input())
                department=input()
                emp_1 = emp(employee_id, first, last,job, salary, department)
                insert_emp(emp_1)
                print ("Registration completed")
            if an1==2:
                print ("Please provide data : Name- Budget -Phone ")
                name=input()
                bud=float(input())
                phone =int(input())
                deploc=  dpto(name, bud, phone)
                insert_dpto(deploc)
                print ("Registration completed")
            if an1==3:
                print ("Please provide data : Employee ID - Net payment- Payment date ")
                id =int(input())
                pag=float(input())
                date=input()
                payan1= paym(id, pag, date)
                insert_pay(payan1)
                print ("Registration completed")
        if ans==2:
            print("Choose an option: ")
            print("1. Update Employee ")
            print("2. Update Department ")
            an1= int(input())
            if an1==1:
                print ("Salary Update")
                print ("Please provide Employee ID : ")
                x=input()
                print ("Please provide new salary : ")
                pay=float(input())
                update_emp(x, pay)
                print ("Update has been succesful")
            if an1==2:
                print ("Budget Update")
                print ("Please name of department : ")
                x=input()
                print ("Please provide new budget : ")
                y=float(input())
                update_dpto (x, y)
                print ("Update has been succesful")
        if ans==3:
            print("Choose an option: ")
            print("1. Delete Employee ")
            print("2. Delete Department ")
            an1= int(input())
            if an1==1:
                print ("Please provide Employee ID")
                x=int(input())
                remove_emp(x)
                print ("Employee register has been deleted ")
            if an1==2:
                print ("Please provide name of Department")
                x=input()
                remove_dpto(x)
                print ("Department register has been deleted ")

        if ans==4:
            print("Choose an option: ")
            print("1. Display Employee ")
            print("2. Display Department ")
            print("3. Display Payment")
            an1= int(input())
            if an1==1:
                print ("Please provide Employee ID : ")
                x=int(input())
                emps = get_emps_by_name(x)
                print ("\nResults :\n ")
                print(emps)
            if an1==2:
                print ("Please provide name of Department : ")
                x=input()
                dpto4 = get_dpto_by_name(x)
                print ("\nResults :\n ")
                print(dpto4)
            if an1==3:
                print ("Please provide Employee ID : ")
                x=int(input())
                pay = get_pay_by_name(x)
                print ("\nResults :\n ")
                print(pay)
        if ans==5:
            exit()

App_UI()
conn.close()
