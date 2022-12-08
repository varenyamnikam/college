def accept_mat(M):
 r=int(input("Enter the value of the row: "))
 c=int(input("Enter the value of the column: "))
 print("\n     Matrix Elements are")   
 for i in range(r):
  A=[]
  for j in range(c):
   A.append(int(input("\n")))
  M.append(A)

def display_mat(m,r,c):
 print("\n       Matrix is: ")   
 for i in range(r):
  for j in range(c):
   print("	  ",m[i][j],end=" ")
  print("\n")  

def displaytrans_mat(m,r,c):
 print("\n       Matrix is: ")   
 for i in range(c):
  for j in range(r):
   print("	  ",m[i][j],end=" ")
  print("\n")      

def Addition(m1,m2,m3,r,c):
 for i in range(r):
  A=[]
  for j in range(c):
   A.append(m1[i][j]+m2[i][j])
  m3.append(A)
    
def Subtraction(m1,m2,m3,r,c):
 for i in range(r):
  A=[]
  for j in range(c):
   A.append(m1[i][j]-m2[i][j])
  m3.append(A)
    
def transpose_mat(m,m1,r,c):
 for i in range(c):
  B=[]  
  for j in range(r):
   B.append(m[j][i])
  m1.append(B)
  
def transposerec_mat(m,m1,r,c):
 for i in range(c):
 
  for j in range(r):
    m1[i][j] = m[j][i]    

def multiplication_mat(M1,M2,M3,r1,c1,c2) :
 for i in range(r1) :
  A = []
  for j in range(c2) :
   sum = 0
   for k in range(c1) :
    sum = sum + (M1[i][k] * M2[k][j])
   A.append(sum)
  M3.append(A)

def main():
 while True:
    
  a = int(input("Enter 1 to start new and 2 to exit: "))  
  if (a==1): 
   print("\n New loop  starts")     
   MAT=[]
   MAT1=[]
   MAT2=[]
   MAT3=[]
   MAT4=[]   
   MAT5=[]
   MAT6=[]

   print("First Matrix:")
   accept_mat(MAT)
   r1=len(MAT)
   c1=len(MAT[0])
   display_mat(MAT,r1,c1)

   print("Second Matrix:")   
   accept_mat(MAT1)
   r2=len(MAT1)
   c2=len(MAT1[0])
   display_mat(MAT1,r2,c2)

   while True:   
    print ("\t1 : Enter 1 Addition of Matrix:")
    print ("\t2 : Enter 2 Subtraction of Matrix :")
    print ("\t3 : Enter 3 Transpose of Matrix:")
    print ("\t4 : Enter 4 Multiplication of Matrix:")
    print ("\t5 : Exit")
    ch = int(input("Enter your choice : "))
    if (ch==1):
     if(r1==r2 and c1==c2):
      Addition(MAT,MAT1,MAT2,r1,c1)
      print("ADDITION OF MATRIX IS : ")
      display_mat(MAT2,r1,c1)
     else:
      print("ADDITION OF MATRIX CANNOT BE PERFORMED")  
   
    elif(ch==2)  :
     if(r1==r2 and c1==c2):
      Subtraction(MAT,MAT1,MAT3,r1,c1)
      print("Subtraction OF MATRIX IS : ")
      display_mat(MAT3,r1,c1)
     else:
      print("Subtraction OF MATRIX CANNOT BE PERFORMED") 
    elif(ch==3):  
     ph = int(input("Enter 1 for  transpose of First Matrix and 2 for Second: "))
     if(ph==1):
      print("Transpose of first matrix is: ")      
      if(r1!=c1) :     
       print("\n     TRANSPOSE OF RECTANGULAR  MATRIX IS : ")
       MAT4= [[0 for x in range(r1)] for y in range(c1)]  
       transposerec_mat(MAT,MAT4,r1,c1)
       displaytrans_mat(MAT4,r1,c1)
      else:
       print("\n     TRANSPOSE OF SQUARE MATRIX IS : ")
       transpose_mat(MAT,MAT4,r1,c1)
       display_mat(MAT4,r1,c1)
     else:
      print("Transpose of Second matrix is: ")        
      if(r2!=c2) :        
       print("\n     TRANSPOSE OF RECTANGULAR  MATRIX IS : ")
       MAT5= [[0 for x in range(r2)] for y in range(c2)]  
       transposerec_mat(MAT1,MAT5,r2,c2)
       displaytrans_mat(MAT5,r2,c2)
      else: 
       print("\n     TRANSPOSE OF SQUARE MATRIX IS : ")
       transpose_mat(MAT1,MAT5,r2,c2)
       display_mat(MAT5,r2,c2) 
    
    elif(ch==4)  :
      if(c1==r2):
       multiplication_mat(MAT,MAT1,MAT6,r1,c1,c2) 
       print("Multiplication OF MATRIX IS : ")
       display_mat(MAT6,r1,c2)
      else:
       print("Multiplication OF MATRIX CANNOT BE PERFORMED") 
   
    else:
     print("loop ended")
     break;
  else:
   print("Exit") 
   break; 
   
main()