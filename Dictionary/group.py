# Group employees by department

employees = [
  {"name": "Tony", "dept": "Sales"},
  {"name": "Gina", "dept": "HR"},
  {"name": "Manny", "dept": "Sales"}
]

d = {i['dept'] : i['name'] for i in employees}

print(d)
