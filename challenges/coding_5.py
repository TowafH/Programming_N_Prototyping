# Towaf Hossain
# PD 1-2
# 3/6/25
# PY Coding Challenge 5

# Fermat's Last Theorem | a**n + b**n = c**n
def check_fermat(a, b, c, n):
    if n <= 2:
        print("Fermat's Last Theorem applies only for n > 2.")
    elif a > 0 and b > 0 and c > 0 and n > 2:
        a_and_b = (a ** n) + (b ** n)
        c_and_n = c ** n
		# Check Fermat's Theorem
        if a_and_b == c_and_n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("Nope, that doesn't work")
    
check_fermat(3, 3, 3, 3)
