"""Phone_book entry point script"""
from phone_book import __app_name__, view

def main():
    #print(__app_name__)
    view.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()


