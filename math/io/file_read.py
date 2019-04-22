#reads and displays contents of a file
def main():
    #open file
    infile = open('philosophers.txt','r')

    #read contents
    file_contents = infile.read()

    #close it
    infile.close()

    #print contents
    print(file_contents)

main()