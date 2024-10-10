names = [
    ["Alice","Bob","Charlie"],
    ["David","Eve","Frank"],
    ["Grace","Heidi","Ivan"],
    ["Judy","Ken","Laura"]
]
names[0].remove("Alice")

for aaaa in names:
        for cute in aaaa:
            print(cute)

new_name = input("Enter name:")
names[0].append(new_name)
print(names)