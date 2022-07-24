def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    length = len(d)
    i = 2
    x = d[1]

    while (i < length):
        x = x + d[i]
        i = i + 1

    x = float(x)
    return x


def percent_to_float(p):
    length = len(p)

    i = 1
    x = p[0]

    while (i < (length - 1)):
        x = x + p[i]
        i = i + 1
    x = float(x)
    x = x / 100
    return x

main()
