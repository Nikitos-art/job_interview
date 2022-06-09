
def deposit_calc(ammount, period, increase):
    total = 0

    if ammount >= 1000 and ammount <= 10000:
        if period == 6:
            total = (ammount / 100 * 5) + ammount + increase * (period - 2)
        if period == 12:
            total = (ammount / 100 * 6) + ammount + increase * (period - 2)
        if period >= 24:
            total = (ammount / 100 * 5) + ammount + increase * (period - 2)

    if ammount > 10000 and ammount <= 100000:
        if period == 6:
            total = (ammount / 100 * 6) + ammount + increase * (period - 2)
        if period == 12:
            total = (ammount / 100 * 7) + ammount + increase * (period - 2)
        if period >= 24:
            total = (ammount / 100 * 6.5) + ammount + increase * (period - 2)

    if ammount > 10000 and ammount <= 100000:
        if period == 6:
            total = (ammount / 100 * 7) + ammount + increase * (period - 2)
        if period == 12:
            total = (ammount / 100 * 8) + ammount + increase * (period - 2)
        if period >= 24:
            total = (ammount / 100 * 7.5) + ammount + increase * (period - 2)

    return total


print(deposit_calc(2000, 36, 350))