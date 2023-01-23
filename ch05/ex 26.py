from math import log


def cc_months_until_paid(balance, apr, payment):
    daily_rate = apr / 365
    answer = (-1/30) * ((log(1 + (balance / payment) * (1 - (1 + daily_rate) ** 30))) / (log(1 + daily_rate)))
    return answer


# rework the formula to give the minimum payment to finish in the given months. no idea how to do this
# def cc_monthly_payment(balance, apr, months):
#     daily_rate = apr / 365
#     answer = (-1/30) * ((log(1 + (balance / payment) * (1 - (1 + daily_rate) ** 30))) / (log(1 + daily_rate)))
#     return answer


b = float(input("Balance: "))
r = float(input("APR: ")) * .01
p = float(input("Monthly payment: "))

print(cc_months_until_paid(b, r, p))
