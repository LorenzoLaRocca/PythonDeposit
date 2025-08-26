def main():
    print('This line is printed directly from the main function of the program')
    secondary_function()

def secondary_function():
    print('This line is printed fro ma secondary funcion call with the main function')

if __name__ == '__main__':
    main()