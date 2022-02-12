deposit = float(input())
period = int(input())
interest = float(input())/100

profit = float(deposit + period * (deposit * interest)/12)

print(profit)
