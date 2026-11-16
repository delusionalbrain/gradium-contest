name = "gunnika"
age = 19
stringex = f"hey! my name is {name} and today i turned {age+1} years old"

print(stringex)

list1 = ["heye","ewf","FEwfw"]
list1.append("edwfr")

dict = {
    "name" : "ggun",
    "age" : 24,
    "class" : "IT1"
}
print(dict["age"])

score = [20,30404,3240,303]

for s in score:
    if s>400 :
        print("well done")
    else:
        print("baddd")

count = 3
while(count>0):
    print(count)
    count-=1

def func(age):
    if(age>18):
        return "yes"
    else:
        return "no"

print(func(20))

with open("fileExample.txt","w") as file:
    file.write("hola")
    file.write("hey")

with open("fileExample.txt", "r") as file:
    content = file.read()
    print(content)

#to set up venv : python3 -m venv .venv
# to activate it: source .venv/bin/activate
# to set up requirements automatically: pip freeze > requirements.txt, keep updating it manually

