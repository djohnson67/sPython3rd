#calculates a retailers sale price
#discount percebnt
DISCOUNT_PERCENTAGE = 0.20

#main func
def main():
    #get regular price
    reg_price = get_regular_price()

    #calculate discount
    sales_price = reg_price - discount(reg_price)

    #print result
    print('The sale price is $', format(sales_price, ',.2f'), sep='')


#prompts user for item's regular price and returns it
def get_regular_price():
    price = float(input('Enter the item\'s regular price: '))
    return price

#accepts an itmes price and returns the discount
def discount(price):
    return price * DISCOUNT_PERCENTAGE

main()
