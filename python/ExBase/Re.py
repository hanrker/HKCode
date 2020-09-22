import re
txt = "China is a great countrycountry 1122"
x = re.search("^China.*country$",txt)
y = re.search("(country){2}$",txt)
if y:
    print("Get it")
    print(y.group())
else:
    print("No")



txt = "I am 20230"
x = re.search(".*[0-9].*$",txt)
print(x)