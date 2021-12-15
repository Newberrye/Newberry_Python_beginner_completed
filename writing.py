employee_file = open("employee.txt", "r+")
print(employee_file.read())

employee_file.write("\nToby - Human Resources")
employee_file.close()


# a and r+ adds to file while w writes a new file or overwrites it