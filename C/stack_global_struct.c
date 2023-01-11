#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 100
typedef struct{
  int student_no;
  char name[MAX_STACK_SIZE];
  char address[MAX_STACK_SIZE];
}element;

element stack[MAX_STACK_SIZE];
int top = -1;

int is_empty(){
  return (top == -1);
}

int is_full(){
  return (top >= (MAX_STACK_SIZE-1));
}

void push(element item){
  if (is_full()){
    fprintf(stderr, "스택이 가득 찼습니다. 삽입이 안됩니다\n");
    return;
  } else{
    stack[++top] = item;
  }
}

element pop(){
  if (is_empty()){
    fprintf(stderr, "스택이 비었습니다.");
    exit(1);
  } else{
    return stack[top--];
  }
}

element peek(){
  if (is_empty()){
    fprintf(stderr, "스택이 비었습니다.");
    exit(1);
  } else{
    return stack[top];
  }
}


int main(void) {

  printf(is_empty() ? "true\n" : "false\n");
  element pugcute = {
    202020, "pugcute", "andong"
  };
  element pop_text;
  push(pugcute);
  printf("%s\n", peek().name);
  pop_text = pop();
  printf("%d\n", pop_text.student_no);
}