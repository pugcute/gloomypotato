#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5

typedef int element;

typedef struct {
	int size;
	element array[MAX_SIZE];
} ArrayList;

void init_array(ArrayList *l) {
	l->size = 0;
}

int is_empty(ArrayList *l) {
	return l->size == 0;
}

int is_full(ArrayList *l) {
	return l->size == MAX_SIZE;
}

element get_entry(ArrayList *l, int idx) {
	if (idx < 0 || idx >= l->size) {
		printf("error\n");
		return 0;
	} else {
		return l->array[idx];
	}
}

void print_array(ArrayList *l) {
	for (int i = 0; i < l->size; i++) {
		printf("->%d", l->array[i]);
	}
  printf("\n");
}

void insert_last(ArrayList *l, int item) {
	if (l->size >= MAX_SIZE) {
		printf("리스트 범위 초과\n");
	} else {
		l->array[l->size++] = item;
	}
}

void insert(ArrayList *l, int index, element item) {
	if (!is_full(l) && (index >= 0) && (index <= l->size)) {
		for (int i = (l->size - 1); i >= index; i--) {
			l->array[i + 1] = l->array[i];
		}
		l->array[index] = item;
		l->size++;
	}
}

void clear(ArrayList *l){
  for (int i = l->size; i>-1; i--){
    l->array[i] = 0; 
  }
  l->size = 0;
}

void replace(ArrayList *l, int index, int item){
  if (index < 0 || index > l->size){
    printf("유효 인덱스가 아닙니다.\n");
  } else{
    l->array[index] = item;
  }
}

element delete (ArrayList *l, int index) {
	if (index < 0 || index >= l->size) {
		printf("유효한 인덱스 아닙니다.\n");
		return 0;
	} else {
		element item;
		item = l->array[index];
		for (int i = index; i < l->size - 1; i++) {
			l->array[i] = l->array[i + 1];
		}
		l->size--;
		return item;
	}
}

int get_length(ArrayList *l){
  return l->size;
}

int main(void) {
	ArrayList list;
  init_array(&list);
	insert(&list, 0, 10);
	print_array(&list);
	insert(&list, 0, 20);
	print_array(&list);
	insert(&list, 0, 30);
	print_array(&list);
	insert(&list, 0, 40);
	print_array(&list);
  insert_last(&list, 70);
  print_array(&list);
  delete(&list, 0);
  print_array(&list);
  printf("%d\n", get_length(&list));
  replace(&list, 4, 90);
  print_array(&list);
  replace(&list, 0, 50);
  print_array(&list);
  


  

  delete(&list, 2);
  print_array(&list);
  

  return 0;
}