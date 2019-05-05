#demo on how to unpickle objects
import pickle

def main():
    #indicate end of file
    end_of_file = False

    #open file for binary
    input_file = open('info.dat', 'rb')

    while not end_of_file:
        try:
            #unpickle next obj
            person = pickle.load(input_file)

            #display
            display_data(person)
        except EOFError:
            #Set eof flag
            end_of_file = True
    
    #close file
    input_file.close()

def display_data(person):
    print('Name: ', person['name'])
    print('Age: ', person['age'])
    print('weight: ', person['weigh'])
    print()

main()