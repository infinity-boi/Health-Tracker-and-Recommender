file1 = open("set.txt", "r")
file2 = open("done.txt", "w")

for line in file1:
    if line[0] < 'A':
        file2.write(line)
    elif line[0]>'Z' and line[0]<'a':
        file2.write(line)
    else:
        file2.write('"' + line.replace("\n", "") + '",')
        
file1.close()
file2.close()
        
    
