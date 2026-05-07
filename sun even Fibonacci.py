def even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
fir = 1
sec = 2

sum = 0

while (fir < 10):
    if even(fir):
        sum = sum + fir
    new = fir + sec
    fir = sec
    sec = new

print(sum)