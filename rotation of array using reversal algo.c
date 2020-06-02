#include <stdio.h>

void reverse(int arr[],int n,int f)
{int i=f,j=n-1,k,temp;
   while(i<j)
  {temp=arr[i];
  arr[i]=arr[j];
  arr[j]=temp;
  --j;
  ++i;
  }
}
void rotate(int arr[],int n,int d)
 { int f=0;
   reverse(arr,d,f);
   reverse(arr,n,d);
   reverse(arr,n,f);
 }
void print(int arr[],int n)
{ int k;
  for(k=0;k<n;k++)
  printf("%d",arr[k]);
}

int main(void) {
  int arr[100],i,n,d;
  scanf("%d",&n);
  for(i=0;i<n;i++)
  scanf("%d",&arr[i]);
  scanf("%d",&d);
  rotate(arr,n,d);
  print(arr,n);
  return 0;
}
