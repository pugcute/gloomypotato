#include <stdio.h>
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MAX_DEGREE 101

typedef struct {
  int degree;
  float coef[MAX_DEGREE];
} polynomial;

polynomial poly_add1(polynomial A, polynomial B) {
  polynomial result;
  int A_idx = 0, B_idx = 0, C_idx = 0;
  int A_degree = A.degree;
  int B_degree = B.degree;
  result.degree = MAX(A_degree, B_degree);
  while (A_idx <= A.degree && B_idx <= B.degree) {
    if (A_degree > B_degree) {
      result.coef[C_idx++] = A.coef[A_idx++];
      A_degree--;
    } else if (A_degree == B_degree) {
      result.coef[C_idx++] = A.coef[A_idx++] + B.coef[B_idx++];
      A_degree--;
      B_degree--;
    } else {
      result.coef[C_idx++] = B.coef[B_idx++];
      B_degree--;
    }
  }
  return result;
}

void printf_poly(polynomial tmp) {
  for (int i = tmp.degree; i > 0; i--) {
    printf("%3.1fx^%d + ", tmp.coef[tmp.degree - i], i);
  }
  printf("%3.1f \n", tmp.coef[tmp.degree]);
}

int main(void) {
  polynomial a = {5, {3, 2, 1, 0, 0, 5}};
  polynomial b = {3, {3, 2, 1, 0}};
  polynomial c;
  c = poly_add1(a, b);
  printf_poly(a);
  printf_poly(b);
  printf_poly(c);
  return 0;
}