from db_utils import add_customer
import requests
import json
from decorators import WaitingDecorator, FormattingStar, Confirm
import re



def get_availability_by_date_and_specialism(date, specialism):
    result = requests.get(
        f'http://127.0.0.1:5000/availability/{date}/{specialism}',
        headers={'content-type': 'application/json'}
    )
    return result.json()


def add_new_booking(_date, advisor, time, first_name, last_name):

    booking = {
         "_date": _date,
         "advisor": advisor,
         "time": time,
         "customer": first_name + " " + last_name,
    }

    result = requests.put(
        'http://127.0.0.1:5000/booking',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )

    return result.json()


def display_availability(records):
    # Print the names of the columns.
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
        'NAME', '09-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17'))
    print('-' * 140)

    # print each data item.
    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            item['name'], item['09-10'], item['10-11'], item['11-12'], item['12-13'], item['13-14'], item['14-15'], item['15-16'], item['16-17']
        ))


def email(first_name):
    terminate = False
    while terminate is False:
        email = input('Please input your email address: ')
        valid = re.search(r'[\w.-]+@[\w.-]+.\w+', email)

        while True:
            if valid:
                print('Welcome', first_name, 'to Sum Experts!')
                terminate = True
                return email

            else:
                print('Sorry this email address is invalid. Please try again.')
                break


@Confirm
@WaitingDecorator
@FormattingStar
def bookingapp(first_name, email):
    print("We will need more information from you first.")
    last_name = input("Please input your last name: ")
    address = input("Please input your address: ")
    phone = input("Please input your phone number: ")
    add_customer(first_name, last_name, address, email, phone)
    specialism = input("Please input one of Mortgage/Investments/FinancialPlanner: ")
    _date = input('Please choose the date. Currently, bookings are only available for November (2022-11-DD): ')
    slots = get_availability_by_date_and_specialism(_date, specialism)
    print('####### AVAILABILITY #######')
    print()
    display_availability(slots)
    print()
    advisor_full = input('Choose an advisor: ')
    advisor = advisor_full.split(" ")[0].capitalize()
    isSuccessful = False

    while not isSuccessful:
        time = input('Choose time based on availability (e.g 11-12): ')
        if slots[0 if advisor == "Phoebe" or advisor == "Julius" or advisor == "Jack" else 1][time] == 'Available':
            add_new_booking(_date, advisor, time, first_name, last_name)
            print(f"Your booking has been successful. Your appointment is on {_date} at {time} with {advisor_full}.")
            print()
            slots = get_availability_by_date_and_specialism(_date, specialism)
            display_availability(slots)
            break
        else:
            print("Booking time unavailable. Please choose other time: ")
