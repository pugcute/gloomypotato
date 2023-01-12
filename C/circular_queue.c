#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 5
typedef int element;
typedef struct {
  element data[MAX_SIZE];
  int front;
  int rear;
}Queue;

void init_queue(Queue *q){
  q->front = 0;
  q->rear = 0;
}

int is_full(Queue *q){
  return (q->rear+1) % MAX_SIZE == q->front;
}

int is_empty(Queue *q){
  return q->front == q->rear;
}

void enqueue(Queue *q, int item){
  if (is_full(q)){
    printf("큐가 가득 찼어요. 삽입불가\n");
  } else{
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = item;
  }
}

element dequeue(Queue *q){
  if (is_empty(q)){
    printf("큐가 비었어요. 삭제불가\n");
    return 0;
  } else{
    q->front = (q->front + 1) % MAX_SIZE;
    return q->data[q->front];
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
  printf("%d %d\n", q.front, q.rear);
  printf("%d %d\n", dequeue(&q), q.front);
  printf("%d %d\n", dequeue(&q), q.front);
  printf("%d %d\n", dequeue(&q), q.front);
  printf("%d %d\n", dequeue(&q), q.front);
  printf("%d %d\n", q.front, q.rear);
  printf(is_empty(&q) ? "큐는 비었어요\n" : "큐에 원소가 있어요\n");
  enqueue(&q, 1);
  printf("%d %d\n", q.front, q.rear);
  enqueue(&q, 2);
  enqueue(&q, 3);
  enqueue(&q, 4);
  printf("%d %d\n", q.front, q.rear);
  printf("%d\n",is_full(&q));
  return 0;
}