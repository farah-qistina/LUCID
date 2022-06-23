# LUCID
A text-based game about lucid dreams

name = input("\ndreamer 1 \nwhat do they call you? \n")
while name.strip() == dreamer1.name or name.strip() = "": 
  name = input("\ninvalid answer \n")
if name.strip() == "qis": dreamer1 = qis()
else: dreamer1 = new(name)
name = input("\ndreamer 2 \nwhat do they call you? \n")
while name.strip() == dreamer1.name: 
  name = input("\ninvalid answer \n")
if name.strip() == "qis": dreamer2 = qis()
else: dreamer2 = new(name)
