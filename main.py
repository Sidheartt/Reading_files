#if the file you named dosen't exit python will make one for you and write

file = open("new_file.txt", mode="w")
# contents = file.read()
# print(contents)
file.write("A Python Developer")


file.close()
