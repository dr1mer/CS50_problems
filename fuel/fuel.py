def main():
    s = input("Fraction: ")
    total = convert(s)   # asign value from convert() eg 75 to total
    print(gauge(total))


def convert(fraction):  #passing the string
    while True:
        try:
            x, y = fraction.split("/")
            x,y = int(x), int(y) # convert to str to int
            z = x/y
            if z<=1:
                p=z*100
                p=round(p)
                return p
            else:
                fraction=input("Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage): # eg pass 75
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"  # 75%


if __name__ == "__main__":
    main()
