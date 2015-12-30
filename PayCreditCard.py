outstanding_balance = float(raw_input("Your outstanding balance: "))
annual_interest_rate = float(raw_input("Your annual interest rate: "))

reset_balance = outstanding_balance

def calculate_updated_balance_per_month(previous_balance, monthly_interest_rate, minimum_monthly_payment ):
    new_balance = previous_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
    return new_balance

month_count = 0
monthly_payment_rate = 10
if_counter = 1
while(outstanding_balance > 0):

    month_count += 1
    outstanding_balance = calculate_updated_balance_per_month(outstanding_balance,(annual_interest_rate/12.0), monthly_payment_rate)

    print "CURRENT BALANCE",
    print outstanding_balance
    print "CURRENT PAYMENT",
    print monthly_payment_rate

    if(month_count >= 12 and outstanding_balance >= 0):
        #count times hit
        if_counter = if_counter + 1
        ##reset balance and month count
        outstanding_balance = reset_balance
        monthly_payment_rate = 10 * if_counter
        month_count = 0
        
        
    
    
print "Months Used: ",
print month_count
print "Current Balance: ",
print outstanding_balance
print "Current monthly payment: ",
print monthly_payment_rate

    
##    
##def calc_balance(outstanding_balance, principal_paid):
##    outstanding_balance -= principal_paid
##    return outstanding_balance
##
##def calc_interest_paid(annual_interest_rate, outstanding_balance):
##    interest_paid = (annual_interest_rate/12.0) * outstanding_balance
##    return interest_paid
##
##def calc_min_month_pay(outstanding_balance, monthly_payment_rate):
##    minimum_monthly_payment = monthly_payment_rate * outstanding_balance
##    return minimum_monthly_payment
##    
##def calc_month_payment(outstanding_balance, monthly_payment_rate):
##    return monthly_payment_rate * outstanding_balance
##
##
##def calc_principle_paid(minimum_monthly_payment, interest_paid):
##
##    principle_paid = minimum_monthly_payment - interest_paid
##    return principle_paid
