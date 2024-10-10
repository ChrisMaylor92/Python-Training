import shutil
import os

src = "Chris's file.txt"
dst = "Chris's rewritten file.txt"

shutil.copy(src, dst)

os.rename("Chris's rewritten file.txt", "Rewrite.txt")



a = open("Rewrite.txt", "r")
print(a.read())
a.close()

print("-----------------------------------------------------------------")

a = open("Rewrite.txt", "w")
a.write("Some new text that totally rewrites the file that i have copied")

a.close()

a = open("Rewrite.txt", "r")
print(a.read())
a.close()
