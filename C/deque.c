#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 5

typedef int element;

typedef struct {
  int front, rear;
  element data[MAX_SIZE];
} Deque;

void init_deque(Deque *d){
  d -> front = 0;
  d -> rear = 0;
}

int is_full(Deque *d){
  return (d->rear + 1) % MAX_SIZE == d->front;
}

int is_empty(Deque *d){
  return d->front == d->rear;
}

void push_front(Deque *d, int item){
  if (is_full(d)){
    printf("덱이 가득찼어요.\n");
  } else{
    d->data[d->front] = item;
    d->front = (d->front-1+MAX_SIZE) % MAX_SIZE;
  }
}

element delete_front(Deque *d){
  if (is_empty(d)){
      printf("덱이 비었어요.\n");
      return 0;
  } else{
    d->front = (d->front + 1) % MAX_SIZE;
    return d->data[d->front];
  }
}

void push_back(Deque *d, int item){
  if (is_full(d)){
    printf("덱이 가득찼어요.\n");
  } else{
    d->rear = (d->rear + 1) % MAX_SIZE;
    d->data[d->rear] = item;
  }
}

element delete_back(Deque *d){
  if (is_empty(d)){
      printf("덱이 비었어요.\n");
      return 0;
  } else{
    int prev = d->rear;
    d->rear = (d->rear-1+MAX_SIZE)% MAX_SIZE;
    return d->data[prev];
  }
}

int main(){
  Deque d;
  init_deque(&d);
  delete_front(&d);
  push_front(&d, 20);
  printf("%d %d\n", d.front, d.rear);
  printf("%d %d %d\n" , delete_back(&d), d.front, d.rear);
  push_back(&d, 10);
  printf("%d %d\n", d.front, d.rear);
  printf("%d %d %d\n" , delete_front(&d), d.front, d.rear);


}
