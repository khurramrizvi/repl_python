var = "too hot to hoot"
print("OG: " + var)
var1 = var
var1 = var1.replace(" ", "")
var1 = var1[::-1]
print("Var1: " + var1)
var = var.replace(" ", "")
print("Var: " + var)
if var == var1:
    print("Matched")
else:
    print("Not matched")
