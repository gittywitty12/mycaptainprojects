#fibonacci numbers using loops

present=0
current=1
for k in range(10):
    print(present)
    final= present+current
    present=current
    current=final
    k+=1
    