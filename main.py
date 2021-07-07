import sys
import decorations
import random
import boolmatr
import warshallops
import numpy as np


def genarray():
    """Generates an array of random 1's and 0's or chosen by the user

    Returns:
        Bool-Type array: An array
    """    
    print('\nPlease input the size of the matrix you want to work with.\n\n')
    m_size, m_size = 2, 2
    try:
        m_size = int(input('Please input how many vertices there are: '))
    except:
        pass

    print('Your values have been set as m = %d and n = %d' % (m_size, m_size))
    usable_array = [[0] * m_size for i in range(m_size)]
    try:
        choice = int(input('Random(1) or selected(2): '))
    except:
        choice = 1

    if choice == 1:
        perc = 0
        print('Creating array...')
        for i in range(0, m_size):
            for j in range(0, m_size):
                usable_array[i][j] = 1 if random.randint(0, 3) == 1 else 0
        decorations.loadingpercentage(0, 100)
        print('\nArray created.')
    else:
        for i in range(0, m_size):
            for j in range(0, m_size):
                try:
                    value = int(
                        input('Please input the value to be used in row %d, column %d: ' % (i, j)))
                    usable_array[i][j] = value if value == 0 or value == 1 else 1
                except:
                    usable_array[i][j] = 0
                finally:
                    for x in range(0, m_size):
                        print(usable_array[x])
    print('\n\nYour array is:\n\n')
    for x in usable_array:
        print(x)
    return usable_array, m_size

try:
    option = int(sys.argv[1])
    if option == 1:
        print('You will calculate using a Boolean Matrix')
        outarray, vertices = genarray()
        newarray = boolmatr.boolmatrixprocedure(outarray, vertices)
        print('Transitive Closure Array:')
        print(newarray)
    elif option == 2:
        print('You will calculate using the Warshall algorithm')
        outarray, vertices = genarray()
        newarray = warshallops.warshall(outarray, vertices)
        if outarray == newarray:
            print('Already on the lowest point')

        print('Transitive Closure Array:')
        for x in newarray:
            print(x)
    else:
        exit(1)
        
    print('Program finished!')
except Exception as e:
    print('=====================Transitive Closure Calculator============================')
    print('\nTo run this program, you must input either 1, 2 or 3:')
    print('1. Calculate using a Boolean Matrix \n2. Calculate using the Warshall algorithm\n')
    exit(1)


# graph = [[0, 0, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]