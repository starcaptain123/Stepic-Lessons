gen = input()
l = len(gen.upper())
cg = gen.upper().count("G")
cc = gen.upper().count("C")
sum = cg + cc
print(sum*100/l)