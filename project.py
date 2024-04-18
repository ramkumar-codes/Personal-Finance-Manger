import datetime
import sys
from tabulate import tabulate
from datetime import timedelta
import yfinance as yf
import re
import csv
import warnings
import time


# Get the current Unix timestamp
current_timestamp = int(time.time())
current_datetime = datetime.datetime.fromtimestamp(current_timestamp, datetime.UTC)

def interface():
    while True:
        print()
        print("Time: ", current_datetime.strftime("%H:%M:%S"))
        print("\nEnter any number on the menu to perform actions:")
        print('1. Expense Manager')
        print('2. Investment Portfolio')
        print('3. Savings Goal Manager')
        print('4. Exit')

        try:
            option = int(input('Enter any option(1-4): '))

            if option == 1:
                expense_manager()
            elif option == 2:
                investment_portfolio()
            elif option == 3:
                savings_manager()
            elif option == 4:
                print("\nThank you for using Personal Finance Manager!\n")
                break
            else:
                print("\nInvalid Input, type(1-4)")
                print_horizontal_line()

        except ValueError:
            print("Invalid input, please enter a valid option (1-4).")

def print_horizontal_line():
    print(75 * "-")

def expense_manager():
    while True:
        print()
        print_horizontal_line()
        print('\t\tExpense Manager')
        print_horizontal_line()
        print()
        print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
        print()
        print("Enter any number on the menu to perform actions:")
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Exit')

        try:
            choice = int(input('Enter any option(1-3): '))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                print("\nThank you for using this manager!")
                break
            else:
                print("\nInvalid Input, type(1-3)")
        except ValueError:
            print("\nInvalid input, please enter a valid option (1-3).")
            print_horizontal_line()

def add_expense(expense_name=None, expense_cost=None, expense_date=None, expense_category=None):

    print()
    print_horizontal_line()
    print('\t\tAdd Expense')
    print_horizontal_line()
    print()
    print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
    print()
    while True:
        try:
            if expense_name is None:
                expense_name = input('Enter the name of the expense: ')
            if expense_cost is None:
                expense_cost = float(input('Enter the cost of the expense: $'))
            if expense_date is None:
                expense_date = input('Enter the date of the expense(yyyy-mm-dd): ')
            if isinstance(expense_cost, float):
                pass
            else:
                raise SystemExit

            if match := re.search(r'(\d+)-(\d+)-(\d+)', expense_date):
                if not len(match.group(1))==4:
                    sys.exit("\nInvalid input, please enter a valid Date.")
                if len(match.group(2))==2:
                    if int(match.group(2))<13 and int(match.group(2))>0:
                        pass
                    else:
                        sys.exit("\nInvalid input, please enter a valid Date.")

                else:
                    sys.exit("\nInvalid input, please enter a valid Date.")


                if len(match.group(3))==2:
                    if int(match.group(3))<32 and int(match.group(3))>0:
                        pass
                    else:
                        sys.exit("\nInvalid input, please enter a valid Date.")

                else:
                    sys.exit("\nInvalid Input, please enter a valid date.")

            else:
                sys.exit("\nInvalid input,please enter a valid Date.")

            if expense_category is None:
                expense_category = input('Enter the category of the expense: ')

        except ValueError:
            sys.exit("\nInvalid input, please enter a valid option.")

        with open ('expenses.csv', 'a') as f:
                if f.tell() == 0:
                    writer = csv.DictWriter(f, fieldnames=["Name", "Cost(in $)", "Date", "Category"])
                    writer.writeheader()
                    writer.writerow({"Name": expense_name, "Cost(in $)": expense_cost, "Date": expense_date, "Category": expense_category})
                else:
                    writer = csv.DictWriter(f, fieldnames=["Name", "Cost(in $)", "Date", "Category"])
                    writer.writerow({"Name": expense_name, "Cost(in $)": expense_cost, "Date": expense_date, "Category": expense_category})
                print('Successfully added.')
                break

def total_expense():
    total_expense = 0
    with open ('expenses.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_expense += float(row['Cost(in $)'])
            total_expense = round(total_expense, 3)
    return total_expense

def view_expenses():
    print()
    print_horizontal_line()
    print('\t\tView Expenses')
    print_horizontal_line()
    print()
    print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
    print()
    print("Expenses:")

    with open ('expenses.csv', 'r') as f:
        reader = csv.DictReader(f)
        i = []
        for row in reader:
            i.append(row)
        print(tabulate(i, headers="keys", tablefmt="grid"))
        print("The total expense is: $", total_expense() )

def investment_portfolio():
    while True:
        print()
        print_horizontal_line()
        print('\t\tInvestment Portfolio')
        print_horizontal_line()
        print()
        print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
        print()
        print("Enter any number on the menu to perform actions:")
        print('1. View Stocks')
        print('2. View Investments')
        print('3. Exit')

        try:
            choice = int(input('Enter any option(1-3): '))
            if choice == 1:
                add_investment()
            elif choice == 2:
                view_investments()
            elif choice == 3:
                print("\nThank you for using this manager!")
                break
            else:
                print("\nInvalid Input, type(1-3)")
        except ValueError:
            print("\nInvalid input, please enter a valid option (1-3).")

def add_investment(ticker_symbol=None, no_of_stocks=None, ask = None):

    print()
    print_horizontal_line()
    print('\t\tAdd Investment')
    print_horizontal_line()
    print()
    print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
    print()
    try:
        if ticker_symbol is None:
            ticker_symbol = input('Enter the ticker symbol of the stock: ')
        start_date = (current_datetime + timedelta(days=-2)).strftime("%Y-%m-%d")
        end_date = (current_datetime + timedelta(days=-1)).strftime("%Y-%m-%d")

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=FutureWarning,)

            stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
            print(tabulate(stock_data, headers="keys", tablefmt="grid"))

            if not ticker_symbol:
                sys.exit("\nInvalid input, please enter a valid ticker symbol.")
        if ask == None:
            ask = input('Do you want to add this stock to your portfolio? (yes/no): ')
    except ValueError:
        sys.exit("Invalid input, please enter a valid option.")

    try:
        if ask == 'yes':
            if no_of_stocks is None:
                no_of_stocks = int(input('Enter the number of stocks: '))
            total_price = stock_data['Close'][-1]*no_of_stocks
            print('The total cost of the investment is: $', stock_data['Close'][-1]*no_of_stocks)
            print('Successfully added.')
            warnings.filterwarnings("ignore", category=FutureWarning)
            with open("investment.csv", "a") as file:
                if file.tell() == 0:
                    writer = csv.DictWriter(file, fieldnames=["Ticker Symbol", "Price (in $)","No's","Total Price", "Date"])
                    writer.writeheader()
                    writer.writerow({"Ticker Symbol": ticker_symbol, "Price (in $)": stock_data['Close'][-1],"No's": no_of_stocks,"Total Price":total_price, "Date": current_datetime.strftime("%Y-%m-%d")})
                else:
                    writer = csv.DictWriter(file, fieldnames=["Ticker Symbol", "Price (in $)","No's","Total Price", "Date"])
                    writer.writerow({"Ticker Symbol": ticker_symbol, "Price (in $)": stock_data['Close'][-1],"No's": no_of_stocks,"Total Price":total_price, "Date": current_datetime.strftime("%Y-%m-%d")})

        else:
            print('Cancelled.')


    except (ValueError, TypeError):
        sys.exit("Invalid input, please enter a valid option.")
    except:
        print("\n\nThe stock is not available today")
def total_investment():
    investment_worth = 0
    with open ('investment.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            investment_worth += float(row['Total Price'])
            investment_worth = round(investment_worth, 2)
    return investment_worth

def view_investments():
    print()
    print_horizontal_line()
    print('\t\tView Investments')
    print_horizontal_line()
    print()
    print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
    print()


    with open ('investment.csv', 'r') as f:
        reader = csv.DictReader(f)
        i = []
        for row in reader:
            i.append(row)
        print(tabulate(i, headers="keys", tablefmt="grid"))
        print(f"The total networth is ${total_investment()}" )

def savings_manager():
    while True:
        print()
        print_horizontal_line()
        print('\t\tSavings Goal Manager')
        print_horizontal_line()
        print()
        print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
        print()
        print("Enter any number on the menu to perform actions:")
        print('1. check your Savings Goal')
        print('2. View Savings Goals')
        print('3. Exit')

        try:
            choice = int(input('Enter any option(1-3): '))
            if choice == 1:
                check_savings_goal()
            elif choice == 2:
                view_savings_goals()
            elif choice == 3:
                print("\nThank you for using this manager!")
                break
            else:
                print("\nInvalid Input, type(1-3)")
        except ValueError:
            print("\nInvalid input, please enter a valid option (1-3).")

def check_savings_goal(principal=None, rate=None, time=None):
    print()
    print_horizontal_line()
    print('\t\tCheck Savings Goal')
    print_horizontal_line()
    print()
    print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
    print()
    try:
        global amount
        amount = 0
        if principal is None:
            principal = float(input('Enter the amount that you want to invest: $'))
        if rate is None:
            rate = float(input('Enter the rate of interest: '))
        if time is None:
            time = float(input('Enter the time period: '))
        amount = principal * (1+(rate/100))**time
        amount = round(amount, 2)
        print("The amount after", time, "years is: $", amount)


    except (ValueError, TypeError):
        sys.exit("\nInvalid input, Please enter the valid details")


    try:
        option = input('Do you want to add this to your savings goal? (yes/no): ')
        if option == 'yes':
            with open("savings.csv", "a") as file:
                if file.tell() == 0:
                    writer = csv.DictWriter(file, fieldnames=["Principal(in $)", "Rate of Interest","Time","Amount(in $)", "Date"])
                    writer.writeheader()
                    writer.writerow({"Principal(in $)": principal, "Rate of Interest": rate,"Time": time,"Amount(in $)":amount, "Date": current_datetime.strftime("%Y-%m-%d")})
                else:
                    writer = csv.DictWriter(file, fieldnames=["Principal(in $)", "Rate of Interest","Time","Amount(in $)", "Date"])
                    writer.writerow({"Principal(in $)": principal, "Rate of Interest": rate,"Time": time,"Amount(in $)":amount, "Date": current_datetime.strftime("%Y-%m-%d")})
                    print('Successfully added.')
        else:
            print('Cancelled.')
    except ValueError:
        sys.exit("\nInvalid input, Please enter the valid details")

def view_savings_goals():
    print()
    print_horizontal_line()
    print('\t\tView Savings Goals')
    print_horizontal_line()
    print()
    print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
    print()
    with open ('savings.csv', 'r') as f:
        reader = csv.DictReader(f)
        i = []
        for row in reader:
            i.append(row)
        print(tabulate(i, headers="keys", tablefmt="grid"))
        print(total_savings())


def total_savings():
    total_savings = 0
    with open ('savings.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_years = float(row['Time'])
            total_savings += float(row['Amount(in $)'])
            total_savings = round(total_savings, 2)
    return (f"The total amount after {total_years} years is: ${total_savings}")



def main():
    global current_date
    current_date = current_datetime.strftime("%Y-%m-%d")
    print()
    print_horizontal_line()
    print('\t\tPersonal Finance Manager')
    print_horizontal_line()
    print('We welcome you to menu-driven interface of the Personal Finance Manager')
    print()
    print("Today's date: ", current_datetime.strftime("%Y-%m-%d"))
    interface()

if __name__ == "__main__":
    main()
