#demo of pickling
import pickle

def main():
    #control loop reps
    again = 'y'

    #open a file for binary writin
    output_file = open('info.dat', 'wb')

    while again.lower() == 'y':
        #get data about person and save
        save_data(output_file)

        #go again"
        again = input('Enter more data? (y/n): ')
    
    output_file.close()

#save_data function
def save_data(file):
    #create person dict
    person = {}

    #getdata and store it
    person['name'] = input('Name: ')
    person['age'] = input('Age: ')
    person['weigh'] = input('Weight: ')

    #pickle the dict
    pickle.dump(person, file)

#call main
main()