f1 = open("sample.txt", "r")
f2 = open("copy.txt", "w")

f2.write(f1.read())

f1.close()
f2.close()