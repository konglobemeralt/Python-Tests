outstanding_balance = raw_input("Your outstanding balance: ")
annual_interest_rate = raw_input("Your annual interest rate: ")

def calculate_monthly_interest_rate(annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12.0
    return monthly_interest_rate

def calculate_updated_balance_per_month(previous_balance, monthly_interest_rate, minimum_monthly_payment ):
    new_balance = previous_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
    return new_balance

def calc_min_month_pay(outstanding_balance, monthly_payment_rate):
    minimum_monthly_payment = monthly_payment_rate * outstanding_balance
    return minimum_monthly_payment


while(new_balance > 0):
    new_balance -= 1
    print new_balance
    

    
    
