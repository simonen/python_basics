pens = int(input()) * 5.8
markers = int(input()) * 7.2
detergent = int(input()) * 1.2

zum = float(pens + markers + detergent)

discount = float(input()) / 100 * zum

final_sum = zum - discount

print(final_sum)
#print(discount)



