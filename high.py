def game():
    return 45


score=game()
with open("file.txt","a")as f:
    f.write(str(score))
    f.write("\n")


with open("file.txt","r")as f:
    n=f.readlines()
    li=[h.strip("\n") for h in n]
    print(li)


li.sort()
print(li)
with open("high_score.txt","w")as f:
    f.write(li[(len(li)-1)])
    print(len(li))
