import json 

employees = []


employees.append({
    "name": "roch",
    "salary":1000,
    "id":1
})

rahul = {
    "name":"rahul",
    "salary":10000,
    "id":2
}

employees.append(rahul)

employees.append({
    "name":"anna",
    "salary":100000,
    "id":3
})


with open ("employee_data.json" , "w" ) as f:
    json.dump(employees,f)

'''

This gives a very big .json files in bytes as compated to protobufs

'''