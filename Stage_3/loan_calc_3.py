#second code
import math

print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")

calc = input()

if calc == 'n':
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('Enter the monthly payment:')
    m_payment = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / 1200
    n = math.ceil(math.log(m_payment / (m_payment - i * loan_principal), 1 + i))
    n_years = math.floor(n / 12)
    n_months = n % 12
    if n_years > 1 and n_months > 1:
        print(f'It will take {n_years} years and {n_months} months to repay this loan!')
    elif n_years == 1 and n_months > 1:
        print(f'It will take {n_years} year and {n_months} months to repay this loan!')
    elif n_years == 1 and n_months == 1:
        print(f'It will take {n_years} year and {n_months} month to repay this loan!')
    elif n_years == 0 and n_months == 1:
        print(f'It will take {n_months} month to repay this loan!')
    elif n_years == 0 and n_months > 1:
        print(f'It will take {n_months} months to repay this loan!')
    elif n_years > 1 and n_months == 0:
        print(f'It will take {n_years} years to repay this loan!')
    elif n_years == 1 and n_months == 0:
        print(f'It will take {n_years} year to repay this loan!')
elif calc == 'a':
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('Enter the number of periods:')
    n_periods = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / 1200
    a = math.ceil(loan_principal * ((i * math.pow((1 + i), n_periods)) / (math.pow((1 + i), n_periods) - 1)))
    print(f'Your monthly payment = {a}!')
elif calc == 'p':
    print('Enter the annuity payment:')
    a_payment = float(input())
    print('Enter the number of periods:')
    n_periods = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / 1200
    p = round(a_payment / ((i * math.pow((1 + i), n_periods)) / (math.pow((1 + i), n_periods) - 1)))
    print(f'Your loan principal = {p}!')