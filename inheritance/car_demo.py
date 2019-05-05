import vehicles

def main():
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.00, 4)

    truck = vehicles.Truck('Toyota',2002,40000,12000.0,'4WD')

    suv = vehicles.SUV('Volvo',2000,30000,18500.0,5)

    #display data
    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model() )
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price())
    print('Doors: ', used_car.get_doors())
    print()

    #display truck
    print('Make: ', truck.get_make())
    print('Model: ', truck.get_model() )
    print('Mileage: ', truck.get_mileage())
    print('Price: ', truck.get_price())
    print('Drive Type: ', truck.get_driver_type())
    print()
    
    #display SUV
    print('Make: ', suv.get_make())
    print('Model: ', suv.get_model() )
    print('Mileage: ', suv.get_mileage())
    print('Price: ', suv.get_price())
    print('Passenger Capacity: ', suv.get_pass_cap())

main()