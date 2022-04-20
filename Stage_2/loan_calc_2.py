JetBrains stages first project 
#first code
print("Enter the loan principal")

principal = int(input())

print('What do you want to calculate?')
print('type "m" for number of monthly payments,')
print('type "p" for the monthly payment:')

proceed = input()

if proceed == 'm':
    print('Enter monthly payment:')
    monthly_payment = int(input())
    monthly = int(principal / monthly_payment + 0.5)
    if monthly == 1:
        print('It will take ' + str(monthly) + ' month to repay the credit')
    else:
        print('It will take ' + str(monthly) + ' months to repay the credit')
elif proceed == 'p':
    print('Enter count of months:')
    count_of_months = int(input())
    payment = - (-principal // count_of_months)
    last_payment = principal - (count_of_months - 1) * round(payment)
    if payment == last_payment:
        print('Your monthly payment = ' + str(payment))
    else:
        print('Your monthly payment = ' + str(payment) + ' with last month payment = ' + str(last_payment))
        
        

