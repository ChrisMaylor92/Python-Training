
a=open("Chris's file.txt", "w")#this overides the file rather than appends it, starting fresh
a.write("My first line in my new file")
a.close()

a=open("Chris's file.txt", "a")
a.write("\nThis is the second line appended to my new file! How awesome is that!")
a.close()


a=open("Chris's file.txt", "a")

x=1
while x < 4:
    
    
    a.write("\nHere is line number " + str(x) + " that I'm adding to my file using a while loop.")
    x+=1
a.close()

with open("Chris's file.txt") as chrisfile:
    print(chrisfile.read()) 


