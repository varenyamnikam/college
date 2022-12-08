def accept(A):
 n=int(input("enter the count of students: "))
 for i in range(n):
  x=int(input("enter the roll no of %d student :"%((i+1))))
  A.append(x)
  
def Display(A):
 p=len(A)
 print("Marks  of students  ")
 for i in range(p):
  print(A[i])
  
def Bubble_sort(A):
 n=len(A)
 for pos in range(n-1):
  for i in range(n-(pos+1)):
   if(A[i]>A[i+1]):
    temp=A[i]
    A[i]=A[i+1]
    A[i+1]=temp

def Selection_sort(A)    :
 n=len(A)
 for pos in range(n-1):
  min_index=pos
  for i in range(pos+1,n):
   if(A[i]<A[min_index]):
    min_index =i
  temp=A[pos]
  A[pos]=A[min_index]
  A[min_index]  =temp
  
def TOP(A):
 n=len(A)
 for pos in range(n-1):
  for i in range(n-(pos+1)):
   if(A[i]<A[i+1]):
    temp=A[i]
    A[i]=A[i+1]
    A[i+1]=temp
    
def Display_TOP(A):
 p=5
 print("Marks  of students  ")
 for i in range(p):
  print(A[i])   
    
    
    
def main():
 P=[]
 Bubble=[]
 Selection=[]
 while True:

  print("Enter 1 for Bubble sort")
  print("Enter 2 for Selection sort")
  print("Enter 3 for TOP Five ")
  print("Enter the 4 for exit")
  ch=int(input("Enter the choice of the to be performed"))
  
 
  if(ch==1):
   accept(P)
   Bubble_sort(P)
   Display(P)
  elif(ch==2):
   accept(P)
   Selection_sort(P)
   Display(P)
  elif(ch==3):
   accept(P)
   TOP(P)
   Display_TOP(P) 
  elif(ch==4):
   break ;
main()