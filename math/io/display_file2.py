#display contents of file
def main():
    #gt name of file
    filename = input("Enter a file name: ")
    try:
        #open the file
        infile = open(filename, 'r')

        #read contents
        contents = infile.read()

        #display contents
        print(contents)

        #close file
        infile.close()
    except IOError:
        print('An error occured trying to read the file ', filename)

main()

