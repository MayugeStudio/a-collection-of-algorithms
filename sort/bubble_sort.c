#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int *arr, size_t count, int *result_arr)
{
  size_t n = count;
  size_t i = 0;
  while (n > 1) {
    if (arr[i] > arr[i+1]) {
      int temp = arr[i];
      arr[i] = arr[i+1];
      arr[i+1] = temp;
    }
    i += 1;
    if (i == n-1) {
      result_arr[n-1] = arr[n-1];
      n -= 1;
      i = 0;
    }
  }
}

#define ARRAY_SIZE(ar) sizeof((ar))/sizeof((ar)[0])

int main(void)
{
  int target[100];
  for (int i = 100; i>0; --i) {
    target[100-i] = i;
  }
  int *result_arr = calloc(100, sizeof(target[0]));
  bubble_sort(target, ARRAY_SIZE(target), result_arr);
  for (size_t i=0; i<ARRAY_SIZE(target); ++i) {
    printf("%lld => %d\n", i, result_arr[i]);
  }
  free(result_arr);
  return 0;
}

