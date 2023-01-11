#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 100
typedef struct{
  int student_no;
  char name[MAX_STACK_SIZE];
  char address[MAX_STACK_SIZE];
}element;

typedef struct{
  element data[MAX_STACK_SIZE];
  int top;
} stack;

void init_stack(stack *s){
  s -> top = -1;
}

int is_empty(stack *s){
  return (s -> top == -1);
}

int is_full(stack *s){
  return (s -> top >= (MAX_STACK_SIZE-1));
}

void push(stack *s, element item){
  if (is_full(s)){
    fprintf(stderr, "스택이 가득 찼습니다. 삽입이 안됩니다\n");
    return;
  } else{
    s->data[++(s->top)] = item;
  }
}

element pop(stack *s){
  if (is_empty(s)){
    fprintf(stderr, "스택이 비었습니다.");
    exit(1);
  } else{
    return s->data[(s->top)--];
  }
}

element peek(stack *s){
  if (is_empty(s)){
    fprintf(stderr, "스택이 비었습니다.");
    exit(1);
  } else{
    return s->data[s->top];
  }
}


int main(void) {
  stack s;
  init_stack(&s);
  printf(is_empty(&s) ? "true\n" : "false\n");
  element pugcute = {
    202020, "pugcute", "andong"
  };
  element pop_text;
  push(&s, pugcute);
  printf("%s\n", peek(&s).name);
  pop_text = pop(&s);
  printf("%d\n", pop_text.student_no);
}