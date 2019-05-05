#reads values from sales.txt
def main():
    #opemn sales
    sales_file = open('sales.txt','r')

    #read first line then test for empty string ''
    line = sales_file.readline()

    #continue until empty string
    while line != '':
        #convert to float
        amount = float(line)

        #print line
        print(format(amount, '.2f'))

        line = sales_file.readline()

    #close file
    sales_file.close()

main()