# external file reading

employee_file = open("employee.txt", "r") # open(path, r.w.a.r+) read,write,append,readwrite

# checks if file is readable
print(employee_file.readable())

# reads file
print(employee_file.read)

# reads first two lines
print(employee_file.readline)
print(employee_file.readline)


#reads all lines in array
print(employee_file.readlines)

# always make sure to close file when done
employee_file.close()