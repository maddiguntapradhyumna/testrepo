empdata={}
min=99999;
max=0
sum=0

for i in range(2):
  emp={}
  emp["id"]=input("Enter emp id")
  emp["name"]=input("Enter emp name")
  emp["basic"]=int(input("Enter emp basic"))
  emp["ta"]=int(input("Enter emp TA"))
  emp["da"]=int(input("Enter emp DA"))
  emp["hra"]=int(input("Enter emp HRA"))
  emp["exp"]=int(input("Enter experience"))
  if emp["exp"]>2:
    emp["bonus"]=int(input("Enter emp bonus "))
  else:
    emp["bonus"]=0
  empdata["emp"+str(i)]=emp

  net=emp['basic']+emp['da']+emp['hra']+emp['ta']+emp['bonus']
  print(emp['name'],"- Net salary :",net)

  if emp['basic']>max:
    max=emp['basic']
    ename=emp['name']
  if emp['basic']<min:
    min=emp['basic']
    ename=emp['name']
    sum+=emp['basic']

print(empdata)
print("Min Salary=",min)
print("Max Salary=",max)
print("Average salary=",sum/2)
