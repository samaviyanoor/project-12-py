file = open("classa.txt")

print(file.read())

file.close()


file = open("classa.txt","r")
print(file.readline(3))
file.close()

file_append=open("classa.txt","a")

file_append.write("\n")

file_append.write ("ali male 17 social studies")

file_append.close()

