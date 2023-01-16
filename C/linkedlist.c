#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode{
  int data;
  struct ListNode *link;
} ListNode;

ListNode* insert_first(ListNode *head, int item){
  ListNode *p = (ListNode *)malloc(sizeof(ListNode));
  p->data=item;
  p->link=head;
  head = p;
  return head;
}

ListNode* insert(ListNode *head, ListNode *pre, int value){
  ListNode *p = (ListNode *)malloc(sizeof(ListNode));
  p->data = value;
  p->link = pre->link;
  pre->link = p;
  return head;
}

ListNode* delete_first(ListNode *head){
  ListNode *removed;
  if (head == NULL) return NULL;
  removed = head;
  head = removed->link;
  free(removed);
  return head;
}

ListNode* delete(ListNode *head, ListNode *pre){
  ListNode *removed;
  removed = pre->link;
  pre->link = removed->link;
  free(removed);
  return head;
}

void print_list(ListNode *head){
  for (ListNode *p = head; p!=NULL; p = p->link){
    printf("%d->", p->data);
  }
  printf("NULL \n");
}

int get_entry(ListNode *head, int index){
  if (index < 0)
		return -1;
  ListNode *tmp;
  tmp = head;
	for (int i = 0; i < index && tmp != NULL; i++){
    tmp = tmp->link;
  }
	return tmp->data;
}

int get_length(ListNode *head){
  ListNode *tmp;
  int length = 0;
  tmp = head;
  if (head == NULL){
    return length;
  }

	for (int i = 0;  tmp != NULL; i++){
    length += 1;
    tmp = tmp->link;

  }
	return length;
}

int find_value(ListNode *head, int value){
  ListNode *tmp = head;
  for (int i = 0; tmp != NULL; i++){
    if (tmp -> data == value){
      return i;
    }
    tmp = tmp -> link;

  }
  return -1;
}

ListNode* reverse(ListNode *head){
  ListNode *p, *q, *r;
  p = head;
  q = NULL;
  while (p!=NULL){
    r = q;
    q = p;
    p = p->link;
    q -> link= r;
  }
  return q;
}

int main(){
  ListNode *head = NULL;

  for (int i=0 ; i<10; i++){
    head = insert_first(head, i);
    print_list(head);
  }
  printf("%d\n", find_value(head, 8));
  printf("%d\n", get_entry(head, 0));
  printf("%d\n", get_length(head));
  printf("%d\n", get_entry(head, 9));

  head = reverse(head);
  print_list(head);
  for (int i = 0; i<10; i++){
    head = delete_first(head);
    print_list(head);
  }


}

