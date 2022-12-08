def accept(name,list):
 x=int(input("enter no. of students in %s "%name))
 for i in range(x):
  y=int(input("enter roll no. of students in %s"%name))
  list.append(y)

def display(list):
  for i in range(len(list)):
    print("\n roll no. %d"%list[i])
def cnb(c,b):
 list=[]
 for i in c:
  if i in b:
   list.append(i)
 return list
def cub(c,b):
 list=[]
 for i in c:
  if i not in b:
   list.append(i)
 for i in b:
  if i not in c:
   list.append(i)

 return list

def main():
  B=[]
  C=[]
  
  accept('batminton',B)
  accept('cricket',C)
  cmn=cnb(C,B)
  cun=cub(C,B)

  display(cun)
main()