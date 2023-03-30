def AñoBisiesto(año):

    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else: 
        return False

print (AñoBisiesto(2020))