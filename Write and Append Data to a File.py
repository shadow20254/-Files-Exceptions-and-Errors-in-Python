# First part , 1 line

print("enter text to write to the file: ")
a=input()
print("data successfully written to file")
b=open("output.txt","w")
b.write(a)
b.close()

#2 part append

print("additional text to append:")
d=input()
c=open("output.txt","a")
c.write("\n"+ d)
c.close()
print("Data successfully appended.")

#final part

print("Final content of output.txt:")
result=open("output.txt","r")
print(result.read())
result.close()



