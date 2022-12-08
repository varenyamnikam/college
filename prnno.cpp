#include <iostream>
#include <string.h>
using namespace std;

struct node {
  int PRN;
  string name;
  node *next, *head = NULL;
  void accept();
  void display();
  void Delete();
  void merge(node obj);
} ob, ob2;

void node::accept() {
  node *p, *temp;
  if (head == NULL) {
    p = new node;

    cout << "Enter president PRN,name";
    cin >> p->PRN;
    cin >> p->name;
    p->next = NULL;
    head = p;
  } else {
    if (head->next == NULL) {
      p = new node;
      cout << "Enter secretary PRN,name:";
      cin >> p->PRN;
      cin >> p->name;
      p->next = NULL;
      head->next = p;
    } else {
      p = new node;
      cout << "Enter member PRN,name:";
      cin >> p->PRN;
      cin >> p->name;
      temp = head;
      while (temp->next->next != NULL) {
        temp = temp->next;
      }
      p->next = temp->next;
      temp->next = p;
    }
  }
}

void node::display() {
  node *temp;
  temp = head;
  while (temp != NULL) {
    cout << temp->PRN << "\t ";
    cout << temp->name << "\n ";
    temp = temp->next;
  }
}

void node::Delete() {
  node *temp, *p;
  cout << "Enter PRN to delete:" << endl;
  int prn;
  cin >> prn;
  if (head->PRN == prn) {
    temp = head;
    head = head->next;
    temp->next = NULL;
    delete temp;
  } else {
    temp = head;
    while (temp->next->PRN != prn) {
      temp = temp->next;
    }
    p = temp->next;
    temp->next = temp->next->next;
    delete p;
  }
}

void node::merge(node obj) {
  node *temp;
  temp = ob.head;
  while (temp->next != NULL) {
    temp = temp->next;
  }
  temp->next = ob2.head;
}

int main() {
  int A;
  cout << "Enter the choices for folowing operations\n";
  cout << "Here are the details of members of Pinacle club" << endl;
  ob.accept();
  ob.accept();
  int n, i;
  cout << "Enter the number of members Pinacle club:\n ";
  cin >> n;
  for (i = 0; i < n; i++) {
    ob.accept();
  }
  ob.display();
  ob.Delete();
  ob.display();

  cout << "Enter details of division B \n";
  ob2.accept();
  ob2.accept();
  int k, z;
  cout << "Enter the number of members Pinacle club:\n ";
  cin >> k;
  for (z = 0; z < k; z++) {
    ob2.accept();
  }
  ob2.display();
  ob.merge(ob2);
  ob.display();

  return 0;
}