import requests
from decorators import WaitingDecorator, FormattingStar, Confirm
from config import MORTGAGE_KEY

@Confirm
@WaitingDecorator
@FormattingStar
def mortgage_calculator():
    amount = input("How much would you like to loan?: ")
    interest_rate = input("Please select an interest rate: ")
    years = input("Please type in number of years?: ")


    api_url = f'https://api.api-ninjas.com/v1/mortgagecalculator?loan_amount={amount}&interest_rate={interest_rate}' \
              f'&duration_years={years}'
    response = requests.get(api_url, headers={"X-Api-Key": MORTGAGE_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        print(f"Your monthly payment is £ {data['monthly_payment']['total']}.")
    else:
        print("Error:", response.status_code, response.text)
