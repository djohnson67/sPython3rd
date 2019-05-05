#demos various set operations
def main():
    baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
    basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

    #display baseball set
    print('The baseball team: ')
    for name in baseball:
      print(name)
    
    #display basketball set
    print('The basketball team: ')
    for name in basketball:
      print(name)
    
    #intersection
    print()
    print('Both teams')
    for name in baseball.intersection(basketball):
      print(name)
    
    #union
    print('Either baseball or basketball')
    for name in baseball.union(basketball):
      print(name)
    
    #differences baseball and basketball
    print('Baseball but not basketball')
    for name in baseball - basketball:
      print(name)
    
    #difference of basketball and baseball
    print('Basketball but not baseball')
    for name in basketball.difference(baseball):
      print(name)

    #symettric difference
    print('One sport but not the other')
    for name in baseball.symmetric_difference(basketball):
      print(name)

main()