emp = [
    {'name': 'prajj', 'dept': 'HR'},
    {'name': 'brij', 'dept': 'IT'},
    {'name': 'kareena', 'dept': 'HR'},
    {'name': 'aryan', 'dept': 'IT'}
]

grp = {}
for emp in emp:
    dept = emp['dept']
    grp.setdefault(dept, []).append(emp['name'])
    print(grp)

print(grp)