from mortgage import mortgage_calculator
from moneylive import livenews
from booking_utils import bookingapp, email

print("""
 _____                   _____                     _       
/  ___|                 |  ___|                   | |      
\ `--. _   _ _ __ ___   | |____  ___ __   ___ _ __| |_ ___ 
 `--. \ | | | '_ ` _ \  |  __\ \/ / '_ \ / _ \ '__| __/ __|
/\__/ / |_| | | | | | | | |___>  <| |_) |  __/ |  | |_\__ \ 
\____/ \__,_|_| |_| |_| \____/_/\_\ .__/ \___|_|   \__|___/
                                  | |                      
                                  |_|                      
""")

first_name = input('Please input your first name: ').strip()
email = email(first_name)
print()

features = True

while features:
    features = input("Please input the number of the service you wish to use: "
                     "\n Calculate a Mortgage - 1 "
                     "\n View Financial News - 2 "
                     "\n Book a meeting with our Financial Advisors - 3: ").strip()
    print()

    if features == '1':
        print (first_name + ', you will now be redirected to our Mortgage Calculator.')
        mortgage_calculator()

    elif features == '2':
        print (first_name + ', you will now be redirected to the current Financial News.')
        livenews()

    elif features == '3':
        print (first_name + ', you will now be redirected to book an online meeting with one of our Advisors.')
        print()
        bookingapp(first_name, email)

    else:
        print ('Sorry', first_name,
               'but those features are unavailable on our app. Please select a valid number.')