with open(sample1,'r') as a:
sample1 = sample1.read()

with open(sample2,'w') as a:
print(sample1)

with open (sample2,'w') as b:
sample2 = sample2.read()

with open(sample1,'r') as b:
print(sample2)