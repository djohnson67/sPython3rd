#writes 3 lines of data to a file
def main():
    #open file
    outfile = open('philosophers.txt','w')

    #write three names
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmend Burke\n')

    #close file
    outfile.close()

#cal main
main()