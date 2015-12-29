
outstanding_balance = int(raw_input("Outstanding Balance: "))
annual_interest_rate = float(raw_input("Annual Interest Rate: "))
monthly_payment_rate = float(raw_input("Monthly Payment Rate: "))

interest_paid = 0
principle_paid = 0
remaining_balance = 0
minimum_monthly_payment = 0

def calc_balance():
    outstanding_balance = outstanding_balance - principal_paid
    return outstanding_balance

def calc_interest_paid():
    interest_paid = (annual_interest_rate/12.0) * outstanding_balance

def calc_principal_paid():
    principal_paid = minimum_monthly_payment - interest_paid

def calc_min_month_pay():
    minimum_monthly_payment = monthly_payment_rate * outstanding_balance
    
def calc_month_payment():
    print monthly_payment_rate * outstanding_balance

def calc_intrest_paid():
    intrest_payed = annual_interest_rate / (12 * outstanding_balance)
    print intrest_payed

def calc_principle_paid():

    principle_paid = minimum_monthly_payment - interest_paid
    print principle_paid
    



for i in range(1, 12):
    
    print "month "
    print i
    print "Monthly Payment "
    calc_month_payment()
    print "Principle Paid "
    calc_min_month_pay()
    calc_interest_paid()
    calc_principle_paid()
    print "Remaning Balance "
    calc_balance()

    
