rent = int(input())

statuettes = rent * 0.7
catering = statuettes * 0.85
sound_sistim = catering * 0.5
expenses = rent + statuettes + catering + sound_sistim

print(f"{expenses:.2f}")
