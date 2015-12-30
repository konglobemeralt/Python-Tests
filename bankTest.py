
outstanding_balance = int(raw_input("Outstanding Balance: "))
annual_interest_rate = float(raw_input("Annual Interest Rate: "))
monthly_payment_rate = float(raw_input("Monthly Payment Rate: "))

interest_paid = 0
principle_paid = 0
remaining_balance = 0
minimum_monthly_payment = 0

def calc_balance(outstanding_balance, principal_paid):
    outstanding_balance -= principal_paid
    return outstanding_balance

def calc_interest_paid(annual_interest_rate, outstanding_balance):
    interest_paid = (annual_interest_rate/12.0) * outstanding_balance
    return interest_paid

def calc_min_month_pay(outstanding_balance, monthly_payment_rate):
    minimum_monthly_payment = monthly_payment_rate * outstanding_balance
    return minimum_monthly_payment
    
def calc_month_payment(outstanding_balance, monthly_payment_rate):
    return monthly_payment_rate * outstanding_balance


def calc_principle_paid(minimum_monthly_payment, interest_paid):

    principle_paid = minimum_monthly_payment - interest_paid
    return principle_paid
    
total_paid  = 0


for i in range(1, 13):
    
    print "month ",
    print i

    print "Monthly Payment "
    minimum_monthly_payment = calc_month_payment(outstanding_balance, monthly_payment_rate)
    print round(minimum_monthly_payment,2)
    
    print "Principle Paid "
    minimum_monthly_payment = calc_min_month_pay(outstanding_balance, monthly_payment_rate)
    interest_paid = calc_interest_paid(annual_interest_rate, outstanding_balance)
    principle_paid = calc_principle_paid(minimum_monthly_payment, interest_paid)
    print round(principle_paid,2)
    
    print "Remaning Balance "
    outstanding_balance = calc_balance(outstanding_balance, principle_paid)
    print round(outstanding_balance,2)

    total_paid += minimum_monthly_payment

print "RESULT"
print "Total Amount Paid: "
print round(total_paid, 2)
print "Remaining Balance: "
print round(outstanding_balance, 2)
