import random
print("***PASSWORD GENERATOR ***")
ucl="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lcl=ucl.lower()
dig="0123456789"
characters="`~!@#$%^&*()[]{}|\:';<.>,?"

upper,lower,nums,syms= True,True,True,True
password=""
if upper:
    password+=ucl
if lower:
    password+=lcl
if nums:
    password+=dig
if syms:
    password+=characters

length=int(input("Enter the length of password you want: "))
passw="".join(random.sample(password,length))
print(f"PASSWORD: {passw}")