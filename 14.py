 
file1 = open(r'C:\Users\Dell\Desktop\python\file.txt','r')
file2 = open(r'C:\Users\Dell\Desktop\python\stop.txt','r')
file3 = open(r'C:\Users\Dell\Desktop\python\file1.txt','a')
for line in file2:
    w = line.split()
    for word in w:
        stoplist.append(word)
#end 
for line in file1:
    w = line.split()
    for word in w:
        if word in stoplist: continue
        else: 
            file3.write(word)
            file3.write(" ")
#end 
file1.close()
file2.close()
file3.close()
