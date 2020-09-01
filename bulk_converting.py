import pandas as pd
import os
import sys

if sys.argv[1] == '' or sys.argv[2] == '' or sys.argv[3] == '' or sys.argv[4] == '':
    print('ERROR: Received insufficient arguments')
    sys.exit(1)

else:

    origin = str(sys.argv[3])
    destination = str(sys.argv[4])
    
    if origin[-1] == '/': pass
    else: origin = origin + '/'
    
    if destination[-1] == '/': pass
    else: destination = destination + '/'
    
    if os.path.isdir(origin) != True:
        print('ERROR: Origin is not a valid directory')
        sys.exit(1)
    
    else:

        if str(sys.argv[1]) == 'csv':
            if str(sys.argv[2]) != 'xlsx': 
                print('ERROR: Unable to convert into specified format.')
                sys.exit(1)
            else:
                list_files = os.listdir(origin)

                if os.path.isdir(destination) == True: pass
                else: os.mkdir(destination)

                for i in list_files:
                    
                    file = pd.read_csv(origin + i, low_memory = False)
                    name, extension = os.path.splitext(i)
                    file.to_excel(destination + name + '.xlsx',
                                header = True,
                                index = False)
                print('Operation sucessful.')
                sys.exit(0)
                    
        elif str(sys.argv[1]) == 'xlsx':
            if str(sys.argv[2]) != 'csv': 
                print('ERROR: Unable to convert into specified format.')
                sys.exit(1)
            else:
                list_files = os.listdir(origin)

                if os.path.isdir(destination) == True: pass
                else: os.mkdir(destination)

                for i in list_files:
                    file = pd.read_excel(origin + i)
                    name, extension = os.path.splitext(i)
                    file.to_csv(destination + name + '.csv',
                                header = True,
                                index = False)
                print('Operation sucessful.')
                sys.exit(0)

        else: 
            print('ERROR: Unable to convert from specified format.')
            sys.exit(1)