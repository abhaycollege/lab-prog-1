end="snippet3\n"

#snippet 1
constructors = ["merc","rb","aston","fer"]
print(constructors)

print(constructors[1:4])
constructors.append("haas")
print(constructors)
constructors.remove("haas")
print(constructors)
print("snippet1\n")

#snippet 2
spells =["abracadabra","wingardium leviosa","expelliarmus","Avada kedarva"]
print(spells[1])
print("snippet 2\n")

#snippet 3

spells =["abracadabra","wingardium leviosa","expelliarmus","Avada kedarva","lumos"]
print(spells[1:4])
print(end)

#snippet4
spells1 =["abracadabra","wingardium leviosa","expelliarmus","Avada kedarva"]
spells1.append("lumos")
print(spells1)
spells1.remove("Avada kedarva")
print(spells1)
print(spells1[1])
print("snippet 4\n")

#snippet 5
person=("abhay",69,"male")
print(person[0])
name,age,gender =person
print(name)
print(gender)
print(age)
print("snippet 5\n")

#snippet 6
spell_tuple=("expectp","expelliarmus","Lumos")
print(spell_tuple)
print("snippet 6\n")

#snippet 7
spell_tuple=("expectp","expelliarmus","Lumos")
print(spell_tuple[1])
print("snippet 7\n")

#snippet 8
spell1 = "expelliarmus"
spell2 = "avada kedarva"
spell3 = "arresto momentum"
spell_tuple=spell1,spell2,spell3
print("spell")
spell1,spell2,spell3=spell_tuple
print(spell3)
print(spell1)
print(spell2)
print("snippet 8\n")

#snippet 9
groceries={
    "eggs": {"quantity":12,"price":3.5},
    "milk": {"quantity":2,"price":2.0}
}
print(groceries["eggs"])

print(groceries.keys())
print(groceries.values())


for item,details in groceries.items():
    print(f"{item}:{details['quantity']} for\${details['price']}")

print("snippet 9\n")

#snippet 10
spell_dict={"expelliarmus":"disarms the op","lumos":"produces light"}
print(spell_dict["expelliarmus"])
print("snippet 10\n")

#snippet 11
spell_dict={"expelliarmus":"disarms the op","lumos":"produces light"}


keys=spell_dict.keys()
print(keys)

values=spell_dict.values()
print(values)

items=spell_dict.items()
print(items)
print("snippet 11\n")

#snippet 12
spell_dict={"expelliarmus":"disarms the op","lumos":"produces light"}

for spell in spell_dict:
    print(spell)

for description in spell_dict.values():
    print(description)




print("snippet 12\n")


with open('shopping_list.txt','w') as file:
    for item,details in groceries.items():
        file.write(f"{item}:{details}\n")
    file.close()

"""
file =open('shopping_list.txt','w')
for item,details in groceries.items():
    file.write(f"{item}:{details}\n")
    """
import csv

def calculate_average(data,column_2):
    total=0
    count=0
    with open(data,"r") as file:
        reader =csv.reader(file)
        for row in reader:
            if len(row) > column_2:
                total += float(row[column_2])
                count +=1

    if count>0:
        average =total/count
        return average
    else:
        raise ValueError("invalid or empty file")

    #test the  func
    filename = "data.csv"
    column_index=2

    try:
        average_value =calculate_average(data,column_2)
        print(f"the average of column{column_2} is{average_value}")
    except ValueError as e:
        print(str(e))
