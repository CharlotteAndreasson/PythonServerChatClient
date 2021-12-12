def main():
    age = 14
    # ...
    if age < 20:
        print("Age is less than 20")
    else:
        print("Age is greater than or equal to 20")

    if age < 20:
        print("Something")
    elif age < 30:
        print("Something else")
    elif age < 40:
        print("More")

    # for-loop
    # for(int i; i < 10; i++)
    for i in range(10):
        print(i)

    for i in range(2, 10, 2):
        print(i)

    values = [3, 45, 6, 55, 78]
    # for(var value : values)
    for value in values:
        print(value)

    generated = list(range(100))
    print(generated)

    # Loops and break
    for value in values:
        if value == 55:
            break
        print(value)
    else:
        print("Inside else")

    for i, value in enumerate(values):
        print(1, value)

    # while
    value = 0
    while value < 10:
        print(value)
        value += 1

    # Python does not have do while

if __name__ == '__main__':
    main()
