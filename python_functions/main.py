def print_greeting():
    print("Hello there")

def main():
    name = 'Charlotte'
    print(type(name))
    name = 14
    print(type(name))

# __name__ contains the string '__main__' if
# if we run this file
# If we import the file it will contain the name of the file
if __name__ == '__main__':
    main()