

employee_file = open("employees.txt", "w") # "a" adding text to the end of the file, "w" overwrite the whole file

employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")

employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()

print(employee_file.read())
employee_file.close()
