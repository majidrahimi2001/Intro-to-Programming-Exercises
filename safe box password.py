def jam_argham(ramz_digits):
    sum_digits = 0
    for k in ramz_digits:
        sum_digits += ramz_digits[k]
    return sum_digits


def ramz_is_ok(ramz_digits):
    if ramz_digits["pa"] + ramz_digits["ce"] == 14 and \
        ramz_digits["ye"] == ramz_digits['do']*2 - 1 and \
            ramz_digits["ch"] == ramz_digits["do"] + 1 and \
                ramz_digits["do"] + ramz_digits["ce"] == 10:
        if jam_argham(ramz_digits) == 30:
            return True
        
for ramz in range(0,100000):
    this_ramz = str(ramz).zfill(5) 
    
    ramz_digits = {}
    ramz_digits["ye"] = int(this_ramz[0])
    ramz_digits["do"] = int(this_ramz[1])
    ramz_digits["ce"] = int(this_ramz[2])
    ramz_digits["ch"] = int(this_ramz[3])
    ramz_digits["pa"] = int(this_ramz[4])
    
    if ramz_is_ok(ramz_digits):
        print(ramz)
        