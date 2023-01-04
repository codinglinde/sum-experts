class WaitingDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("Please wait while we process your request.")
        self.function(*args, **kwargs)
        print("Request processed.")
        print()
        confirmation_menu = input('Would you like to go back to the main menu? (y/n): ')
        if confirmation_menu.lower() == "n":
            features = False
            print("Goodbye!")
            exit(1)
        else:
            features = True


class FormattingStar:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("=" * 75)
        print()
        self.function(*args, **kwargs)
        print()
        print("=" * 75)


class Confirm:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        confirmation = input(f"Would you like to proceed? (y/n): ")
        if confirmation.lower() == "y":
            self.function(*args, **kwargs)
        else:
            print("Goodbye!")
            exit(1)
