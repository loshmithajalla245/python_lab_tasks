f = open("sample.txt", "r")
text = f.read()
f.close()

print("Lines:", len(text.splitlines()))
print("Words:", len(text.split()))
print("Characters:", len(text))