from datetime import datetime
from datetime import date
import copy

# import mortgage

current_month = datetime.now().month
current_year = datetime.now().year

# print current_month
# print type(current_year)
# loan_amount = float(input("Enter loan amount: "))
# years = input("Enter years for loan payment: ")
# rate = input("Enter rate of interest: ")
# loan_start_month = input("Enter loan start month(1 to 12): ")
# loan_start_year = input("Enter loan start year, skip (press enter) for current year : ") or current_year

loan_amount = float(5000000)
years = 20
rate = 10
loan_start_month = 1
loan_start_year = 2020

tax_rebate_interest_part = 350000
year_months =12

loan_amount_copy = copy.deepcopy(loan_amount)
monthly_rate_of_interest = float(rate)/(100*12)

total_periods = 12 * float(years)
monthly_emi = ((loan_amount)*(monthly_rate_of_interest)*(((1+monthly_rate_of_interest)**total_periods)/(((
    1+monthly_rate_of_interest)**total_periods)-1)))


print "monthly emi is Rs {emi}".format(emi=monthly_emi)
total_months = 12* years
total_tax_benefit = 0

'''
Calculation for first and last year is a bit different than rest
'''
if loan_start_month <=3:
    first_year_months_before_fy_start = 3 - loan_start_month
elif loan_start_month > 3:
    first_year_months_before_fy_start = 3 + (12 - loan_start_month)

year_count = 0
for each_month in range(1,total_months+1):
    this_year_interest = (rate*loan_amount_copy)/100
    monthly_interest_payment = this_year_interest/12
    monthly_principal_payment = monthly_emi - monthly_interest_payment
    loan_amount_copy =  loan_amount_copy - monthly_principal_payment
    if each_month == first_year_months_before_fy_start:
        print "First FY Year ended"
        year_count = year_count + 1
        first_year_principal_amount = monthly_principal_payment * first_year_months_before_fy_start
        first_year_interest_amount = monthly_interest_payment * first_year_months_before_fy_start
        print "You paid Rs {p} as Principal amount ".format(p=first_year_principal_amount)
        print "You paid Rs {p} as Interest amount ".format(p=first_year_interest_amount)
        if first_year_interest_amount <= tax_rebate_interest_part:
            tax_benefit_first_year = first_year_interest_amount
        else:
            tax_benefit_first_year = tax_rebate_interest_part
        print "You will get tax_benefit of Rs {p} ".format(p=tax_benefit_first_year)
        total_tax_benefit = total_tax_benefit + tax_benefit_first_year
    
    elif each_month == first_year_months_before_fy_start + 12*year_count:
        year_count = year_count + 1
        print "FY year {y} ended".format(y=year_count)
        this_year_principal_amount = monthly_principal_payment * year_months
        this_year_interest_amount = monthly_interest_payment * year_months
        print "You paid Rs {p} as Principal amount ".format(p=this_year_principal_amount)
        print "You paid Rs {p} as Interest amount ".format(p=this_year_interest_amount)
        if this_year_interest_amount <= tax_rebate_interest_part:
            tax_benefit_this_year = this_year_interest_amount
        else:
            tax_benefit_this_year = tax_rebate_interest_part
        print "You will get tax_benefit of Rs {p} ".format(p=tax_benefit_this_year)
        total_tax_benefit = total_tax_benefit + tax_benefit_this_year

print "Total tax benefit is {tax_benefit}".format(tax_benefit=total_tax_benefit)



