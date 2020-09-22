x = 5
y = 4
z = "han"
#define function 
def myfunc2():
    x = 4
    print(x+y)
#execute function
myfunc2()

def GetType(x):
    print(type(x))
GetType(z)

#引入随机模块
import random
print(random.randrange(1,4))

#多行字符串
multi = """ss
sds  
sdsdfdf
是的地方
fg """
print(multi[-1])

#去除字符串前后空白字符
st = " qwe,ss "
print(st)
print(st.strip())
#替换字符
print(st.replace("q","s"))
print(st.split(","))

isThere = "qw" in st
print(isThere)

#合并字符串与数值
i = 3
j = 4
st = "我是{},{},{}"
st2 = "我是{1},{0}"

#st3 = "我是{2},{1}"  语法错误j
# print(st)
print(st.format(i,j,j))
# print(st2.format(i,j))
#print(st3.format(i,j))


#ifss
a = 4
b = 6
print("sss")
if a < b:
    print("asb")
else:
    print("a==b")

#元组
htuple = ("han","rui","kai","HKS")
print(htuple[1:3])
for x in htuple:
    print(x)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset2 = {"apple1", "banana", "cherry1"}
print(thisset.update( {"apple1", "banana", "cherry1"}))

#字典
thisDic = {
    "name":"han",
    "sex":"male",
    "year":30,
}

thisDic["year"] = 40
x = thisDic["year"]
print(x)
for j  in thisDic:
    print(thisDic[j])


#if else
a = 200
b = 66
# if a > b: print("a is greater than b")
print("A") if a > b else print("B") 

a = 200 
b = 100
c = lambda a,b:a+2*b
print(c(1,2))

#类
class h:
    def __init__(self,name,age):
       self.name  = name
       self.age = age
    def pp(self):
        print(self.name)
c1 = h("hsn",12)
c1.pp() 

#子类
class Parent:
    def __init__(self,name,age):
       self.name  = name
       self.age = age
    def pp(self):
        print(self.name)
class Child(Parent):
    pass
i = Child("han",78)
i.pp()

#模块
import python.quote as s
s.greeting("s1s")

#日期
import datetime
x = datetime.datetime.now()
print(x.month)
y = datetime.datetime(2020,4,3)
print(y)

#jason
import json

x = {
  "name": "Bill",
  "age": 63,
  "married": True,
  "divorced": False,
  "children": ("Jennifer","Rory","Phoebe"),
  "pets": None,
  "cars": [
    {"model": "Porsche", "mpg": 38.2},
    {"model": "BMW M5", "mpg": 26.9}
  ]
}

print(json.dumps(x,indent=2))

#正则
import re

txt = "China is a great country"
x = re.search("^China.*country$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")


print("Enter your name:")
x = raw_input()
print("Hello ", x)

#file
import os
f = open(".\content.txt")
print(f.read(1))

print("ss")