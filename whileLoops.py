statement = "Great Job!"
x = 1

while x <= 3:
    print(statement)
    x += 1

print("<_______________________________>\n")



#continue statements make the loop skip the iteration that matches the condition, moving onto the next iteration
#break statements stop the loop once the condition has been met
z = 0
while z < 10:
    z += 1  
    if z == 3:
        print("We have skipped three")
        continue  
    print(z)
    if z == 6:
        print("We are stopping now")
        break
    
