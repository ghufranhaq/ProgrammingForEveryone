hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate per Hours:")
r = float(rate)

diff = (h-40)

if h <= 40:
    pay = (h * r)
    print(pay)

elif h >= 40:
 rateabove40 = (1.5 * r)*diff
 dif = (diff * rateabove40)
 Pay40 = (h-diff) * r + rateabove40

 #pay = (h * r) +
 print(Pay40)
