#gets employee data and saves it
def main():
    #number of employee records to save
    num_emps = int(input('How many employee records do you want to create? '))

    #open file for writing
    emp_file = open('employees.txt', 'w')

    #get data and write it
    for count in range(1, num_emps + 1):
        #get employee data
        print('Enter data for employee #',count,sep='')
        name = input('Name: ')
        id_numb = input('ID Number: ')
        dept = input('Department: ')

        #write to file
        emp_file.write(name + '\n')
        emp_file.write(id_numb+'\n')
        emp_file.write(dept+'\n')

        #blank line
        print()

    #close file
    emp_file.close()
    print('Employee info written to file')

main()



