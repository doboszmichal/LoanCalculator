import math
import argparse


def main():
    what_to_calculate()


def what_to_calculate():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["annuity", "diff"])
    parser.add_argument("--payment")
    parser.add_argument("--principal")
    parser.add_argument("--periods")
    parser.add_argument("--interest")
    args = parser.parse_args()
    credit_parts = [args.type, args.payment, args.principal, args.periods, args.interest]

    if credit_parts[0] == "annuity":
        if not credit_parts[4]:
            print("Incorrect parameters")
        elif not credit_parts[1]:
            calculate_mont_payment(credit_parts[2], credit_parts[3], credit_parts[4])
        elif not credit_parts[3]:
            calculate_how_long(credit_parts[2], credit_parts[1], credit_parts[4])
        else:
            calculate_annuity(credit_parts[1], credit_parts[3], credit_parts[4])
    elif credit_parts[0] == "diff":
        if not credit_parts[4]:
            print("Incorrect parameters")
        else:
            calculate_diff(credit_parts[2], credit_parts[3], credit_parts[4])



def calculate_diff(principal, periods, interest):
    principal = int(principal)
    periods = int(periods)
    interest = float(interest)
    nominal_interest_rate = ((interest / 100) / (12 * 1))
    sum = 0
    count = 0
    for i in range(1, periods + 1):
        payment = (principal / periods) + nominal_interest_rate * (principal - (principal * (i - 1)) / periods)
        # print("Month {}: payment is {}".format(i, int(payment)))
        if payment % (int(payment)) != 0:
            sum = sum + payment + 1
            print("Month {}: payment is {}".format(i, int(payment)+1))
        else:
            sum = sum + payment
            print("Month {}: payment is {}".format(i, int(payment)))
            count = count + 1
    overpayment = sum - principal - count
    print("Overpayment = {}".format(int(overpayment)))


def calculate_annuity(payment, periods, interest):
    payment = int(payment)
    periods = int(periods)
    interest = float(interest)
    nominal_interest_rate = ((interest / 100) / (12 * 1))
    loan_principal = (payment / ((nominal_interest_rate * (pow((1 + nominal_interest_rate), periods))) / (pow((1 + nominal_interest_rate), periods)-1)))
    overpayment = payment * periods - loan_principal + 1
    print("Your loan principal = {}!".format(int(loan_principal)))
    print("Overpayment = {}".format(int(overpayment)))


def calculate_mont_payment(principal, periods, interest):
    principal = int(principal)
    periods = int(periods)
    interest = float(interest)
    nominal_interest_rate = ((float(interest) / 100) / (12 * 1))
    monthly_payment = principal * ((nominal_interest_rate * pow((1 + nominal_interest_rate), periods)) / (pow((1 + nominal_interest_rate), periods) - 1))
    if monthly_payment % (int(monthly_payment)) != 0:
        print("Your monthly payment = {}!".format(int(monthly_payment)+1))
    else:
        print("Your monthly payment = {}!".format(int(monthly_payment)))


def calculate_how_long(principal, payment, interest):
    principal = int(principal)
    payment = int(payment)
    interest = float(interest)
    nominal_interest_rate = ((interest / 100) / (12 * 1))
    base = 1 + nominal_interest_rate
    x = (payment / (payment - nominal_interest_rate * principal))
    number_of_month = math.log(x, base)
    number_of_month = int(number_of_month + 1)
    if number_of_month == 1:
        print("It will take 1 month to repay this loan!")
    elif number_of_month < 12:
        print("It will take {} months to repay this loan!".format(int(number_of_month)))
    elif number_of_month == 12:
        print("It will take 1 year to repay this loan!")
    elif 12 < number_of_month < 24:
        months = number_of_month % 12
        if months == 1:
            print("It will take 1 year and 1 month to repay this loan!")
        else:
            month = months % 12
            print("It will take 1 year and {} months to repay this loan!".format(int(month)))
    elif number_of_month >= 24:
        years = int(number_of_month // 12)
        if number_of_month % 12 == 0:
            print("It will take {} years to repay this loan!".format(int(years)))
        elif number_of_month % 12 == 1:
            print("It will take {} years and 1 month to repay this loan!".format(int(years)))
        elif number_of_month % 12 > 1:
            print("It will take {} years and {} months to repay this loan!".format(int(years), int(number_of_month % 12)))
    overpayment = number_of_month * payment - principal + 1
    print("Overpayment = {}".format(int(overpayment)))


if __name__ == '__main__':
    main()
