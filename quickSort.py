def main():
 Per=[]
 accept(Per)
 #display(Per)
 n=len(Per)
 Quick_sort(Per,0,n-1)
 display(Per)

 top(Per)



def accept(A):
 n=int(input("Enter the total no of Element : "))
 for i in range(n):
  a=float(input("Enter the elements "))
  A.append(a)


def display(A)  :
 for i in range(len(A)):
  print("Elements of the list are: ",A[i])
 print("\n")
 
def top(A):
 n=len(A)
 if(n<=5):
  print("top 5 are : ",A[::-1])
 else:
  print("Top 5 are : ",A[:n-6:-1]) 
   
 
def partition(A,lb,ub):
 i=lb+1
 j=ub
 while(i<=j):
  while(i<=j and A[lb]>=A[i]):   #while(i<=j and A[lb]<=A[i]):
   i=i+1
  while(A[lb]<A[j]):   #while(A[lb]>A[j]):
   j=j-1
  if(i<j):
   temp=A[i]
   A[i]=A[j]
   A[j]=temp
 temp=A[lb]
 A[lb]=A[j]
 A[j]=temp
 return j
  
  
def Quick_sort(A,lb,ub)       :
 if(lb<ub):
  mid=partition(A,lb,ub)
  Quick_sort(A,lb,mid-1)
  Quick_sort(A,mid+1,ub)
 
main()