values = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8,
          "white": 9}
values2 = {0: "black", 1: "brown", 2: "red", 3: "orange", 4: "yellow", 5: "green", 6: "blue", 7: "violet", 8: "grey",
           9: "white"}
mytype = input()
if mytype == "str":
    centaine = input()
    dizaine = input()
    unite = input()
    print(str(values[centaine]) + str(values[dizaine]) + str(values[unite]))
else:
    val = input()
    if len(val) < 3:
        for _ in range(3 - len(val)):
            val = "0" + val
    print(str(values2[int(val[0])]) + str(values2[int(val[1])]) + str(values2[int(val[2])]))
