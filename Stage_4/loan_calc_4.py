#third code
import math
import argparse


def periods_to_year(periods):
    date_str = ""
    years = periods // 12
    months = periods % 12
    if years > 1 and months > 1:
        date_str = f"{years} years and {months} months"
    elif years > 1 and months == 1:
        date_str = f"{years} years and {months} month"
    elif years == 1 and months > 1:
        date_str = f"{years} year and {months} months"
    elif years == 1 and months == 1:
        date_str = f"{years} year and {months} month"
    elif years == 0 and months > 1:
        date_str = f"{months} months"
    elif years == 0 and months == 1:
        date_str = f"{months} month"
    elif years > 1 and months == 0:
        date_str = f"{years} years"
    elif years == 1 and months == 0:
        date_str = f"{years} year"
    return date_str


def number_of_monthly_payments(l_principal, month_payment, ln_interest):
    nominal_interest_rate = ln_interest / (12 * 100)
    periods = math.ceil(math.log((month_payment / (month_payment - nominal_interest_rate * l_principal)), 1 + nominal_interest_rate))
    result_string = f"It will take {periods_to_year(periods)} to repay this loan!"
    total_sum = periods * month_payment
    result_string += f"\nOverpayment = {int(total_sum - l_principal)}"
    return result_string


def monthly_payment(payment_type, l_principal, periods, ln_interest):
    nominal_interest_rate = ln_interest / (12 * 100)
    result_string = ""
    total_sum = 0
    if payment_type == "annuity":
        month_payment = math.ceil(l_principal * nominal_interest_rate * pow(1 + nominal_interest_rate, periods) / (pow(1 + nominal_interest_rate, periods) - 1))
        result_string = f"Your monthly payment = {month_payment}!"
        total_sum = periods * month_payment

    elif payment_type == "diff":
        for i in range(periods):
            month_payment = math.ceil(l_principal / periods + nominal_interest_rate * (l_principal - l_principal * (i + 1 - 1) / periods))
            total_sum += month_payment
            result_string = result_string + f"Month {i+1}: payment is {month_payment}\n"
    result_string += f"\nOverpayment = {int(total_sum - l_principal)}"
    return result_string


def loan_principal(payment, periods, ln_interest):
    nominal_interest_rate = ln_interest / (12 * 100)
    l_principal = round(payment / (nominal_interest_rate * pow(1 + nominal_interest_rate, periods) / (pow(1 + nominal_interest_rate, periods) - 1)))
    result_string = f"Your loan principal = {l_principal}!"
    total_sum = periods * payment
    result_string += f"\nOverpayment = {int(total_sum - l_principal)}"
    return result_string


def main_menu():
    user_choice = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" - for annuity monthly payment amount,
type "p" -for loan principal:
""")
    if user_choice == "n":
        print("Enter the loan principal:")
        l_principal = float(input())
        print("Enter the monthly payment:")
        month_payment = float(input())
        print("Enter the loan interest:")
        loan_interest = float(input())
        print(choice_dict[user_choice](l_principal, month_payment, loan_interest))
    elif user_choice == "a":
        print("Enter the loan principal:")
        l_principal = int(input())
        print("Enter the number of periods:")
        number_of_periods = int(input())
        print("Enter the loan interest:")
        ln_interest = float(input())
        print(choice_dict[user_choice](l_principal, number_of_periods, ln_interest))
    elif user_choice == "p":
        print("Enter the annuity payment:")
        annuity_payment = float(input())
        print("Enter the number of periods:")
        number_of_periods = int(input())
        print("Enter the loan interest:")
        ln_interest = float(input())
        print(choice_dict[user_choice](annuity_payment, number_of_periods, ln_interest))


choice_dict = {'n': number_of_monthly_payments,
               'a': monthly_payment,
               'p': loan_principal}
parser = argparse.ArgumentParser(description="This program calculates differentiated or annuity loan payments.")
parser.add_argument("--type",  choices=["diff", "annuity"], help="You need to choose only one type of payment because they are excluding.")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()
options = [args.type, args.principal, args.periods, args.interest, args.payment]
options_length = len([el for el in options if el is not None])
is_negative = len([True for el in options if el is not None and el != "diff" and el != "annuity" and float(el) < 0])

if not args.type or not args.interest:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
elif options_length < 4 or is_negative:
    print("Incorrect parameters")
elif args.type and args.principal and args.payment and args.interest and not args.periods:
    print(number_of_monthly_payments(float(args.principal), float(args.payment), float(args.interest)))
elif args.type and args.principal and not args.payment and args.interest and args.periods:
    print(monthly_payment(args.type, float(args.principal), int(args.periods), float(args.interest)))
elif args.type == "annuity" and not args.principal and args.payment and args.interest and args.periods:
    print(loan_principal(float(args.payment), int(args.periods), float(args.interest)))