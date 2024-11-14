import json

# parsing json : converting json string to python dictionary
json_string = '{"name": "John", "age": 30, "city": "New York"}'
parsed_json = json.loads(json_string)
print("the name of the person is: ", parsed_json['name'])
# we used the loads() method to parse the json string and convert it into a python dictionary

# converting python dictionary to json string
python_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(python_dict)
print("the json string is: ", json_string)
# we used the dumps() method to convert the python dictionary into a json string

# writing json to a file
