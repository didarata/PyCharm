#lets pretend there is file employees.txt with list of names

employee_file = open("employees.txt", "r")    #this is how you open i file just to read, no modification no changes

print(employee_file.readable())      #this is how we check if files is readable
print(employee_file.read())          #will print all the information in the file
print(employee_file.readline())
print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()



open("employees.txt", "w")    #in this mode you can write new information and chnage excisting information
open("employees.txt", "a")    #you can add new information to the end of the file
open("employees.txt", "r+")   #read and write, all power of reading and writing

