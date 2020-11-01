import pyodbc
import time

#Read
def read(conn):
    print()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customer.dbo.Customer')
    for row in cursor:
        print(row)
    print()

#Create
def create(conn, firstName, lastName, age):
    cursor = conn.cursor()
    cursor.execute(
        "insert into Customer.dbo.Customer (FirstName,LastName,Age) values ('"+firstName+"','"+lastName+"',"+str(age)+");"
    )
    conn.commit()
    print()

#Update First Name
def updateFirstName(conn, nameToChange, firstName, lastName, age):
    cursor = conn.cursor()
    cursor.execute(
        "update Customer.dbo.Customer set FirstName = ? where (FirstName = ? AND LastName = ? AND Age = ?);",
        (nameToChange, firstName, lastName, str(age))
    )
    conn.commit()
    print()

#Update Last Name
def updateLastFirstName(conn, lastNameToChange, firstName, lastName, age):
    cursor = conn.cursor()
    cursor.execute(
        "update Customer.dbo.Customer set LastName = ? where (FirstName = ? AND LastName = ? AND Age = ?);",
        (lastNameToChange, firstName, lastName, str(age))
    )
    conn.commit()
    print()

#Update Age
def updateAge(conn, ageToChange, firstName, lastName, age):
    cursor = conn.cursor()
    cursor.execute(
        "update Customer.dbo.Customer set Age = ? where (FirstName = ? AND LastName = ? AND Age = ?);",
        (ageToChange, firstName, lastName, str(age))
    )
    conn.commit()
    print()

#Delete
def delete(conn, firstName, lastName, age):
    cursor = conn.cursor()
    cursor.execute(
        'delete from Customer.dbo.Customer where (FirstName = ? AND LastName = ? AND Age = ?);',
        (firstName, lastName, str(age))
    )
    conn.commit()
    print()

#Request Name
def requestFirstName():
    print()
    firstNameLoop=True
    firstName=''
    while (firstNameLoop):
        print('Please put in the first name:')
        firstName = input()
        if (firstName == ''):
            print('Invalid first name!')
        else:
            firstNameLoop=False
    print()
    return firstName

#Request Last Name
def requestLastName():
    print()
    lastNameLoop=True
    lastName=''
    while (lastNameLoop):
        print('Please put in the last name:')
        lastName = input()
        if (lastName == ''):
            print('Invalid last name!')
        else:
            lastNameLoop=False
    print()
    return lastName

#Request Age
def requestAge():
    ageLoop=True
    age=0
    while (ageLoop):
        print('Please put in the age:')
        try:
            age = int(input())
            if (age>120):
                print('Invalid age!')
            elif (age<1):
                print('Invalid age!')
            else:
                ageLoop=False
        except Exception as e:
            print('Please input a number')
    print()
    return age










#Program Starts
server = 'LOKI\JEANDATABASE'
database = 'jean'
password = 'Jmjmjm_1993'
Database = 'Customer'
Driver = '{ODBC Driver 17 for SQL Server}'


conn = pyodbc.connect('Driver='+Driver+';'
                      'Server='+server+';'
                      'Database='+Database+';'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

menuLoop = True
nameLoop = True

while menuLoop:
    print('Would you like to:\n1.) Read the records in the database.\n2.) Create a new database record.\n3.) Update an existing record in the database.\n4.) Delete a record from the database.\n5.) Quit the program.')
    choice = input()

    if(choice == '1'):
        print()
        read(conn)

    elif(choice == '2'):
        firstName = requestFirstName()
        lastName = requestLastName()
        age = requestAge()
        create(conn, firstName, lastName, age)

    elif(choice == '3'):
        firstName = requestFirstName()
        lastName = requestLastName()
        age = requestAge()
        print('Would you like to:\n1) change the user name.\n2) Change the user last name.\n3) Change the user age.')
        while nameLoop:
            choiceName = input()
            if(choiceName == '1'):
                print("Please enter the new first name:")
                nameToChange = input()
                updateFirstName(conn, nameToChange, firstName, lastName, age)
                nameLoop = False
            elif(choiceName == '2'):
                print("Please enter the new last name:")
                lastNameToChange = input()
                updateLastFirstName(conn, lastNameToChange, firstName, lastName, age)
                nameLoop = False
            elif(choiceName == '3'):
                print("Please enter the new age:")
                ageToChange = input()
                updateAge(conn, ageToChange, firstName, lastName, age)
                nameLoop = False
            else:
                print("Please put in a valid input")
        nameLoop = True

    elif(choice == '4'):
        firstName = requestFirstName()
        lastName = requestLastName()
        age = requestAge()
        delete(conn, firstName, lastName, age)

    elif(choice == '5'):
        menuLoop=False
        print("Goodbye")
        time.sleep(2)
    else:
        print("Please put in a valid input")

conn.close()
