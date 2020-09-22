import json
x = '{ "name":"han","age":13,"city":"SJZ"}'
y = json.loads(x)
print(y["name"])

x1 = { "name":"han","age":13,"city":"SJZ"}
y1 = json.dumps(x1,indent=1)
y2 = json.dumps(x1,indent=4,separators=(". ", " = "),sort_keys=True)
print(y1,y2)



print(json.dumps({"name": "Bill", "age": 63}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))