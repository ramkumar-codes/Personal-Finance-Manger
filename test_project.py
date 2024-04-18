import pytest
from project import *  # Importing functions from project1 module
import warnings

# Ignore all warnings for testing purposes
warnings.filterwarnings('ignore')

# The following tests are designed to check the behavior of various functions in your project1 module


def test_add_expense_invalid_input():
    """
    Test the behavior of add_expense function with invalid input.
    """
    # Test adding an expense with invalid input for cost
    expense_name = "Groceries"
    expense_cost = "invalid"  # Invalid cost
    expense_date = "2024-02-20"
    expense_category = "Food"

    # Call the function and expect a SystemExit exception due to invalid input
    with pytest.raises(SystemExit):
        add_expense(expense_name, expense_cost, expense_date, expense_category)

    # Test adding an expense with an invalid date format
    expense_name = "Groceries"
    expense_cost = 600.00
    expense_date = "2024-02-2000"  # Invalid date format
    expense_category = "Food"

    # Call the function and expect a SystemExit exception due to invalid input
    with pytest.raises(SystemExit):
        add_expense(expense_name, expense_cost, expense_date, expense_category)


def test_add_investment():
    """
    Test the behavior of add_investment function with invalid input.
    """
    # Test adding an investment with invalid input for number of stocks
    ticker_symbol = "AAPL"
    no_of_stocks = "sdf"  # Invalid input for number of stocks
    ask = "yes"

    # Call the function and expect a SystemExit exception due to invalid input
    with pytest.raises(SystemExit):
        add_investment(ticker_symbol, no_of_stocks, ask)


def test_check_savings():
    """
    Test the behavior of check_savings_goal function with invalid input.
    """
    # Test checking savings goal with invalid input for principal amount
    principal = 1000  # Valid principal amount
    rate = 'asdf'      # Invalid input for interest rate
    time = 10

    # Call the function and expect a SystemExit exception due to invalid input
    with pytest.raises(SystemExit):
        check_savings_goal(principal, rate, time)

    # Test checking savings goal with invalid input for principal amount
    principal = 'asdf'  # Invalid input for principal amount
    rate = 10            # Valid interest rate
    time = 10

    # Call the function and expect a SystemExit exception due to invalid input
    with pytest.raises(SystemExit):
        check_savings_goal(principal, rate, time)
