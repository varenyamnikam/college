#include<iostream>
using namespace std;

struct queos
{ 
   int data;
   queos *job;
   queos *next;
   queos *front=NULL;
   queos *rear=NULL;
   void addjob();
   void deljob();
   void displayjob();
};

void queos::addjob(){
    if(rear==NULL){
     queos *p;
     p=new queos;
     cout<<"enter the job:";
     cin>>p->data;
     rear=p;
     front=p;
     p->next=NULL;
     
    }
    else{
     queos *p;
     p=new queos;
     cout<<"enter the job:";
     cin>>p->data;
     rear->next=p;
     rear=p;
     
    }
}

void queos::displayjob(){
   queos *i;
   i=front;
   
   while(i!=NULL){
   cout<<i->data<<" ";
    i=i->next;
   
    }
    cout<<"\n";
}
void queos::deljob(){
   if(front==NULL){
    cout<<"element is underflow";
   }
   else{
    queos *p;
    p=front;
    front=front->next;
    delete p;
   }
}
int main(){
   queos obj;
  char ch;
  
  do
  {
    obj.addjob();

    cout << "want to continue?";
    cin >> ch;
  } while (ch == 'y'|| ch=='Y');
  obj.displayjob();
  obj.deljob();
  obj.displayjob();


}