import csv, sys, re

def main():
    try: 
        if len(sys.argv) < 2:
            print("add a filename")
        elif len(sys.argv) > 2:
            print("too many arguements")
        elif len(sys.argv) == 2:
            filename = sys.argv[1]
            if re.search(r'\.csv$', filename, re.IGNORECASE):
                create_blank_cvs(filename)
            else:
                print("wrong filename extension")
    except Exception as e:
        sys.exit(e)
        
def create_blank_cvs(filename):
    '''
    Create a blank csv file with the given filename
    
    Parameters
    ----------
    filename : str
        The name of the file to create
    '''
    with open(filename, 'w', newline='') as csvfile:
        pass

if __name__ == '__main__':
    main()