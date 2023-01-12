#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 5

typedef int element;
typedef struct{
  int front;
  int rear;
  element data[MAX_SIZE];
} Queue;

void init_queue(Queue *q){
  q->front = -1;
  q->rear = -1;
}

int is_full(Queue *q){
  if (q->rear==MAX_SIZE-1)
    return 1;
  else
    return 0;
}

int is_empty(Queue *q){
  if (q->front == q->rear)
    return 1;
  else
    return 0;
}

void enqueue(Queue *q, int item){
  if (is_full(q)){
    printf("큐가 가득찼습니다.");
    return;
  } else{
    q->data[++(q->rear)] = item;
  }
}

int dequeue(Queue *q){
  if (is_empty(q)){
    printf("큐가 비었습니다.");
    return -1;
  } else{
    int item = q->data[++(q->front)];
    return item;
  }
}

int main(){
  int item = 0;
  Queue q;

  init_queue(&q);
  enqueue(&q, 10);
  enqueue(&q, 20);
  enqueue(&q, 30);
  enqueue(&q, 40);
  enqueue(&q, 50);
  printf("%d %d\n", q.front, q.rear);
  printf("%d %d\n", dequeue(&q), q.front);
  printf("%d %d\n", dequeue(&q), q.front);
  printf("%d %d\n", dequeue(&q), q.front);
  printf("%d %d\n", dequeue(&q), q.front);
  printf("%d %d\n", dequeue(&q), q.front);
  printf("%d %d\n", q.front, q.rear);
  printf(is_empty(&q) ? "큐는 비었어요\n" : "큐에 원소가 있어요\n");
  enqueue(&q, 1);
  return 0;

}