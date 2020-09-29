from pyfy import Pyfy

myfin= Pyfy()

rate_percent = 5/12
rate = rate_percent/100
number_of_years = 2
n = number_of_years*12

fv = 0
pv = -100000

x = {"rate":rate, "n":n, "pv":pv, "fv":fv, "options":"pmt"}
myfin.calculate(x)
# # when
# # {{'begin', 1}, {'end', 0}}
#
# # # fv(rate, nper, pmt, pv[, when])
# print("fv=")
# print(fin.fv(rate, n, pmt, pv))
# # # pv(rate, nper, pmt[, fv, when])
# print("pv=")
# print(fin.pv(rate, n, pmt, fv))
# # # pmt(rate, nper, pv[, fv, when])	Compute the payment against loan principal plus interest.
# # pmt = 1444.92
# print("pmt=")
# x = {"rate":rate, "nper":n, "pv":pv, "fv":fv}
# print(fin.pmt(rate=rate, nper=n, pv=pv, fv=fv))
#
# # # nper(rate, pmt, pv[, fv, when])	Compute the number of periodic payments.
# print("n=")
# print(fin.nper(rate, pmt, pv, fv))
# # # rate(nper, pmt, pv, fv[, when, guess, tol, …])	Compute the rate of interest per period.
# print("rate=")
# print(fin.rate(n, pmt, pv, fv))




# npv(rate, values)	Returns the NPV (Net Present Value) of a cash flow series.

# ppmt(rate, per, nper, pv[, fv, when])	Compute the payment against loan principal.
# ipmt(rate, per, nper, pv[, fv, when])	Compute the interest portion of a payment.
# irr(values)	Return the Internal Rate of Return (IRR).
# mirr(values, finance_rate, reinvest_rate)	Modified internal rate of return.

