file = open('inputfile.txt','r')
passFile = open('passFile.txt','w')
failFile = open('failFile.txt','w')
for line in file:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)
    
file.close()
passFile.close()
failFile.close()