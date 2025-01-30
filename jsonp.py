import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json

# a Python object (dict):
x = '{"name": "John","age": 30, "city": "New York"}'

# convert into JSON:
y = json.loads(x)

# the result is a JSON string:
print(y['name'])

def solve():
    n = [1,2,3,4,5,3]
    a = max(n)
    b = n.remove(a)
    print(b)
    c = max(n)
    print(c)
    
solve()
    
