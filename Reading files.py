#reading files
# <r> opens a file in read-only mode while the file offset stays at the root
# <w> opens the file in both read and write modes while the file offset is again at the root level, so it overwrites anything in the file
# <a> opens the fil in append mode. The offset goes to the end of the file. if the file doesnt exist then it gets created.
# <x> creates a file and throws an error if the file already exists

print("Reading Files")

print("-----------------------------------------------------")


a = open("demo.txt", "r")

print(a.read())
a.close()

print("-----------------------------------------------------")

b = open("demo.txt", "r")

print(b.readline())
b.close()

print("-----------------------------------------------------")
#with opens and closes the file, as creates a variable
with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

print("-----------------------------------------------------")

a=open("demo.txt", "a")
a.write("\nHere is another line our text file")
a.close()

print("-----------------------------------------------------")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

print("-----------------------------------------------------")

a=open("demo.txt", "w")
a.write("What is happening now")
a.close()

a = open("demo.txt", "r")

print(a.read())
a.close()

print("-----------------------------------------------------")




with open("Chris's file.txt") as chrisfile:
    contents = chrisfile.read()
    print(contents)

a=open("Chris's file.txt", "w")
a.write("My first line in my new file")
a.close()

a=open("Chris's file.txt", "a")
a.write("\nThis is the second line appended to my new file! How awesome is that!")
a.close()

x=0
while x < 4:
    x+=1
    a=open("Chris's file.txt", "a")
    a.write("\nAdding three repeating lines to my file using a while loop.")
    a.close()

with open("Chris's file.txt") as chrisfile:
    contents = chrisfile.read()
    print(contents) 


