#csv 
#comma separated values


#open()
#if we open using this open() we have to manually close it 


#r -->read
#a -->append
#w -->write
#x -->create
#t -->text
#b -->bunary mode(image etc)
# f =open("hello.txt","x")


# with open("hello.txt","w") as f:
#     f.write("wow hello world!")


# with open("hello.txt") as f:
#     print(f.read())


# with open("hello.txt","r") as f:
#     print(f.read())


#write line ()
# f=open("hello.txt","a")
# f.writelines(["\n see you  \n over and over"])
# f.close()

# f=open("hello.txt","r")
# print(f.read())


#csv 
#comma separated values

# import csv
# with open("newfile.csv","w",newline="")as file:
#     w=csv.writer(file)
#     w.writerow(["no","movies","author"])
#     w.writerow(["1","lord of the rings","frongo benhin"])
#     w.writerow(["2","Harry potter","J K rowlling"])

#     #reading 
# with open("newfile.csv","r")as file:
#     reader =csv.reader(file)
#     for row in reader:
#         print(row)

#Append
# with open("protogonist.csv","a",newline=)as f:
#     writer=csv.write(file)
#     writer.writer row(new_row)



#creatinng a zip file
# import zipfile
# with zipfile.ZipFile("text.zip","w")as f:
#     f.write("newfile.csv")
#     f.write("protogonist.csv")

#unzip 
# import zipfile
# with zipfile.ZipFile("text.zip","r")as f:
#     f.extractall(" my extracted")
#     list1=f.namelist()
#     print(list1)





