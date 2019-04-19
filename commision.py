#calculates sales commisions

#control the loop
keep_going = 'y'

#calculate series of commisions
while keep_going == 'y':
    #get a salespeson sales and commision rates
    sales = float(input('Enter the amount of the sales: '))
    comm_rate = float(input('Enter the commision rate:'))

    #calc the commisions
    commission = sales*comm_rate

    #display commision
    print('The commision is $', \
        format(commission, ',.2f'), sep = '')
    
    #do another?
    keep_going = input('Do another commission (Enter \'y\' for yes): ')