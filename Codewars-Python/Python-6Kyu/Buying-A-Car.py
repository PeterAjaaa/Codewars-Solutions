# Link to kata: https://www.codewars.com/kata/554a44516729e4d80b000012

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    end_month = 0
    old_value = 0
    new_value = 0
    saving = savingperMonth
    
    if startPriceOld >= startPriceNew:
        return [end_month, startPriceOld-startPriceNew]

    while True:
        if end_month == 0: # Checks if it's the end of the 1st month.
            old_value = startPriceOld - (startPriceOld * percentLossByMonth / 100)
            new_value = startPriceNew - (startPriceNew * percentLossByMonth / 100)
            total_value = (old_value - new_value) + savingperMonth
            end_month += 1

        elif (end_month + 1) % 2 == 0: # Checks if the month is even.
            percentLossByMonth += 0.5
            old_value -= (old_value * percentLossByMonth / 100)
            new_value -= (new_value * percentLossByMonth / 100)
            saving += savingperMonth
            total_value = (old_value - new_value) + saving
            end_month += 1
            
        elif (end_month + 1) % 2 != 0: # Checks if the month is odd.
            old_value -= (old_value * percentLossByMonth / 100)
            new_value -= (new_value * percentLossByMonth / 100)
            saving += savingperMonth
            total_value = (old_value - new_value) + saving
            end_month += 1
            
        if total_value > 0:
            break

    return [end_month, round(total_value)] # Return the value of 'end_month' and rounded 'total_value'.
