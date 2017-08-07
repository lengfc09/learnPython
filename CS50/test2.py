import datetime


def main():
    dd = get_string()
    print("working here on with {}".format(dd), datetime.date.today())


def get_string():
    x = input("type your name here \n")
    return x
# the reason we put it here is to make sure all the functions are callable
if __name__ == "__main__":
    main()
else:
    print(__name__)
