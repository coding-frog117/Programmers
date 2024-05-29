string = input()

croatia=["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in croatia:
  string = string.replace(i,"K")

print(len(string))