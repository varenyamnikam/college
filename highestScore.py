def accept(A):                                                                                              
 n=int(input("enter the number of students in the class: "))
 for i in range(n):
  while True:
   x=input("enter the marks of %d - student: "%(i+1))
   if x=="AB":
    
    x=-1
    break;
   x=int(x)
   if(x>=0 and x<=30):
    break;
   else:
    print("enter valid marks or student is absent")                                          
  A.append(x)

def display(A):
 p=len(A)
 print(" marks of student present  ")
 for i in range(p):
  if(A[i]==-1):
   print("absent")
  else:
   print(A[i])  
   
def average(A):
 sum=0;
 count=0;
 for i in range(len(A)):
  if(A[i]!=-1):
   count+=1
   sum=sum+A[i]
 avg=sum/len(A)
 print("average is %.2f"%avg)  
 print("no of students absent %d"%(len(A)-count))
 
def max_min(A):
 max=-1;
 min=31;
 for i in range(len(A)):
  if(max<A[i]):
   max=A[i]
   max_index=i
  if(min>A[i] and A[i]!=-1) : 
   min=A[i]
   min_index=i
 print("maximun score is %d"%max)
 print("minimun score is %d"%min)
    
def high_Frequency(A):
 freq = 0
 for i in range(len(A)) :
  tally = 0
  if(A[i] != -1) :
   for j in range(len(A)):
    if(A[i] == A[j]) :
     tally += 1
  if(freq < tally) :
   Marks = A[i]
   freq = tally
 print("\nMarks with highest frequency is %d (%d)"%(Marks,freq))
    
def main():
 FDS=[]
 accept(FDS)    
 display(FDS)

 while True:  
  print ("\t1 : Enter 1 for the average of FDS and students absent for FDS:")
  print ("\t2 : Enter 2 of the  Highest score and lowest score of class :")
  print ("\t3 : Enter 3 to Display mark with highest frequency:")
  print ("\t5 : Exit")
  ch = int(input("Enter your choice : "))

  if (ch==1):
   average(FDS)
  elif (ch==2):
   max_min(FDS)
  elif (ch==3):
   high_Frequency(FDS)
  else:
   print("loop ended")
   break;
  
main() 