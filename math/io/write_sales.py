#prompts for sales and writes to sales.txt
def main():
    #get number of days
    num_days = int(input('For how many days do you have sales? '))

    #open sales file
    sales_file = open('sales.txt','w')

    for count in range(1, num_days +1):
        #get sales for day
        sales = float(input('Enter sales for day #' + str(count) + ': '))

        #write sales to txt
        sales_file.write(str(sales)+ '\n')
        
    #close file
    sales_file.close()
    print('Data written to sales.txt')

main()