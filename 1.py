def accept(A,st):
 n=int(input("enter the count of studentsfor %s: "%st))
 for i in range(n):
  x=int(input("enterthe roll no of %d student for %s:"%((i+1),st)))
  A.append(x) # append is used to store the value in list
 
def Display(A,st):
 p=len(A)
 print("roll number of students playing %s"%st)
 for i in range(p):
  print(A[i])

def search(R,x):
 for i in range(len(R)):
  if (R[i]==x):
   return (1)
 return (0)

def diff(A,B,E):
 for i in range(len(A)):
  flag=search(B,A[i]) # flag defines a value which may be true or false
  if (flag==0):
   E.append(A[i])
   
def union(A,B,F):
 for i in range(len(A)):
  F.append(A[i])
 for i in range(len(B)):
  flag=search(A,B[i])
  if (flag==0):
   F.append(B[i])
   
def universal(F,D,G):
 for i in range(len(F)):
  G.append(F[i])
 for i in range(len(D)):
  flag=search(F,D[i])
  if (flag==0):
   G.append(D[i])

def intersection(A,B,C):
 for i in range(len(A)):
  flag=search(B,A[i])
  if (flag==1):
   C.append(A[i])  
   
def main():
 Group_A=[]
 Group_B=[]
 Group_D=[]
 Group_C=[]
 Group_E=[]
 Group_F=[]
 Group_G=[]
 Group_H=[]
 Group_I=[]
 Group_J=[]
 Group_K=[]
 Group_L=[]
 
 accept(Group_A,"cricket")
 Display(Group_A,"cricket")
   
 accept(Group_B,"badminton")
 Display(Group_B,"badminton")
   
 accept(Group_D,"football")
 Display(Group_D,"football")
   
 union(Group_A,Group_B,Group_F)

 universal(Group_F,Group_D,Group_G)
#  Display(Group_G,"universal")

 while True:  
  print ("\t1 : List of students who play both cricket and badminton:")
  print ("\t2 : List of students who play either cricket or badminton but not both:")
  print ("\t3 : Number of students who play neither cricket nor badminton:")
  print ("\t4 : Number of students who play cricket and football but not badminton:")
  print ("\t5 : Exit")
  ch = int(input("Enter your choice : "))
   
  if (ch==1):
     intersection(Group_A,Group_B,Group_C)
     Display(Group_C,"Cricket and Badminton")
  elif (ch==2):
     diff(Group_F,Group_C,Group_E)
     Display(Group_E,"either cricket or badminton but not both")
   
  elif (ch==3):  
     diff(Group_G,Group_A,Group_H)
#       Display(Group_H,"union")

     diff(Group_G,Group_B,Group_I)
    #  Display(Group_I,"union")
   
     intersection(Group_H,Group_I,Group_J)
     Display(Group_J,"neither cricket nor badminton")

  elif (ch==4):
     intersection(Group_A,Group_D,Group_K)
    #  Display(Group_K,"intersection")

     diff(Group_K,Group_B,Group_L)
     Display(Group_L,"cricket and football but not badminton.")
  else:
    print("loop ended")
    break;
    
main()