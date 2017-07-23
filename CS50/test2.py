import datetime
def main():
    print("working here on", datetime.date.today())


def get_string():
    x = input("type your name here \n")
    return x
# the reason we put it here is to make sure all the functions are callable
if __name__ == "__main__":
    main()
else:
    print(__name__)
