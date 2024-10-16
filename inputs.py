txt = input ("can you see this? Yes or No?")
print("You said: ", txt)
    
txt = input ("Hey, give me a number: ")
try:
    num = int(txt)
    print("The number you gave is: ", num)
except ValueError:
    print("Please put in a number, not text")



salary = 26000
txt = "You could start on over £{} a year!"
print(txt.format(salary))

string = "Chris likes {} {}"
print (string.format("beatboxing", "drum and bass"))


string2 = "Chris loves {}{} and has {} {}"
print(string2.format("boxing", "kids", 0, "beat"))

string2 = "Chris loves {2}{0} and has {amount} {1}"
print(string2.format("boxing", "kids", "beat", amount = 0))

print("Chris loves {2}{0} and has {amount} {1}".format("boxing", "kids", "beat", amount = 0))
