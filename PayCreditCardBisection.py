outstanding_balance = float(raw_input("Your outstanding balance: "))
annual_interest_rate = float(raw_input("Your annual interest rate: "))

monthly_payment_lower_bound = outstanding_balance / 12.0
monthly_payment_upper_bound = (outstanding_balance * (1 + annual_interest_rate / 12.0) ** 12.0)/12.0

guess = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2

remain = outstanding_balance

## precision variable
epsilon = 0.10 

##reset save variable
reset_balance = outstanding_balance

def calculate_updated_balance_per_month(previous_balance, monthly_interest_rate, minimum_monthly_payment ):
    new_balance = previous_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
    return new_balance



while(remain >= epsilon):

    guess = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2
    print guess
    for i in range(1,13):

        new_balance = remain - guess
        month_interest = annual_interest_rate /12 * new_balance
        remain = new_balance+ month_interest

    if(remain < 0):
        monthly_payment_upper_bound = guess
        remain = reset_balance

    elif(remain > epsilon):
        monthly_payment_lower_bound = guess
        remain = reset_balance

    print i
    
print "Lowest Payment: %.2f" %(guess)
