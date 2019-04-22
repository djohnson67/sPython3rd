#reads file oneline at a time and strips \n from it
def main():
    infile = open('philosophers.txt','r')

    #read 3 lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #striup \n from each line
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    #close it
    infile.close()

    #print the data from mem
    print(line1)
    print(line2)
    print(line3)

#call the main function
main()