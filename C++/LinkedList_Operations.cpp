#include<bits/stdc++.h>
using namespace std;
struct Node
{
	int data; 
	Node *next ;
	Node(int x){
		data = x; 
		next = NULL; 
	} 
}*head = NULL,*ptr= NULL,*head1=NULL,*head2 =NULL;
void print(Node *head){
	Node *ptr = head;
	while(ptr!=NULL){
		cout<<ptr->data<<"->";
		ptr = ptr->next; 
	}
	cout<<endl; 
}
void insert(int x,Node* head){
    Node *temp = new Node(x) ;  
    if(head == NULL){
        head = temp; 
    }else{
        Node *ptr = head; 
        while(ptr->next != NULL){
            ptr = ptr->next; 
        }
        ptr->next = temp; 
    }
}
void insertAtbeg(int x){
	Node *temp = new Node(x); 
	temp->next = head; 
	head = temp; 
}
void insertAtend(int x){
	Node *temp = new Node(x); 
	Node *ptr= head; 
	while(ptr->next!=NULL){
		ptr= ptr->next; 
	}
	ptr->next = temp; 
}
void deleteAnyNode(int x){ 
	Node *ptr= head; 
	int length =0,position =  0; 
	while(ptr->next!=NULL){
		ptr= ptr->next;
		length++;  
		if(ptr->data == x){
			position = length; 
		}
	}
	if(position ==0 ){
		head = head->next; 
	}
	else { 
		ptr = head;
		position-=1;
		int i=0;
		while(position != i){
			i++; 
			ptr= ptr->next;
		}
		if(ptr->next->next!=NULL){
			ptr->next = ptr->next->next; 
		}
		else{
			ptr->next = NULL; 
		}
	}
}
Node* reverseAlinkedlist(Node* head){
	Node * prev_p = NULL; 
	Node * current_p = head; 
	Node * next_p; 
	while(current_p){
		next_p = current_p->next; 
		current_p->next = prev_p; 
		prev_p = current_p; 
		current_p = next_p; 
	}
	head = prev_p; 
	return head; 
}
Node* middleoflinkedlist(Node* head){
	Node *ptr =head; 
	int n=0; 
	while(ptr){
		ptr= ptr->next; 
		n++; 
	}
	ptr= head; 
	for(int i=0;i<n/2;i++){
		ptr =ptr->next; 
	}
	return ptr; 

}
Node* mergeTwoSortedLinkedList(Node* head ,Node*head1, Node*head2){
	Node *ptr = head;
	Node *ptr1 = head1; 
	Node *ptr2 = head2; 

	while(ptr1 and ptr2){
		if(ptr1->data> ptr2->data){
			insert(ptr2->data,head); 
		}
		else{
			insert(ptr1->data,head); 
		}
	}
	if(ptr1){
		insert(ptr2)
	}
	if(ptr2){

	}
}
int main(){

	insert(10,head);
	insert(20,head);
	insert(30,head);
	insert(40,head);
	print(head); 
	insertAtbeg(0); 
	print(head); 
	insertAtend(100); 
	print(head); 
	deleteAnyNode(20); 
	print(head);
	head  = reverseAlinkedlist(head); 
	print(head); 
	ptr = middleoflinkedlist(head); 
	cout<<ptr->data<<endl; 
	insert(3,head1);
	insert(4,head1);
	insert(9,head1);
	insert(10,head1);
	insert(1,head2);
	insert(2,head2);
	insert(5,head2);
	insert(6,head2);
	insert(7,head2);
	insert(8,head2);
	head = NULL; 
	ptr = mergeTwoSortedLinkedList(head,head1,head2); 
	print(ptr); 

	return 0; 
}
