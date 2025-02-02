import json
#convert a python dictionary in a json string
data={"name":"john","age":10}
json_data=json.dumps(data)
print(f"json data:{json_data}")
#parse a json string into a python dictionary
parsed_data=json.loads(json_data)
print(f"parsed_data:{parsed_data}")