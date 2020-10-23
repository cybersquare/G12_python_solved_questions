# Remove all the lines that contain the character 'a' in a file and write it
# to another file. 

file = open('hash.txt', "r")



copy_file = open('copy.txt', "w")

lines = file.readlines()
for line in lines:
    if 'a' not in line:
        copy_file.write(line)

file.close()
copy_file.close()

