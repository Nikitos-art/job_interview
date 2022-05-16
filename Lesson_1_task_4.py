
def deposit_calc(ammount, period):
    total = 0

    if ammount >= 1000 and ammount <= 10000:
        if period == 6:
            total = (ammount / 100 * 5) + ammount
        if period == 12:
            total = (ammount / 100 * 6) + ammount
        if period >= 24:
            total = (ammount / 100 * 5) + ammount

    if ammount > 10000 and ammount <= 100000:
        if period == 6:
            total = (ammount / 100 * 6) + ammount
        if period == 12:
            total = (ammount / 100 * 7) + ammount
        if period >= 24:
            total = (ammount / 100 * 6.5) + ammount

    if ammount > 10000 and ammount <= 100000:
        if period == 6:
            total = (ammount / 100 * 7) + ammount
        if period == 12:
            total = (ammount / 100 * 8) + ammount
        if period >= 24:
            total = (ammount / 100 * 7.5) + ammount

    return total

print(deposit_calc(2000, 36))