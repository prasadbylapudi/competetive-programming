
#include <stdio.h>
int p, q, n,count=0;
int main()
{
	scanf("%d", &q);// total no of numbers u input
	scanf("%d",&p);// number to divisible
	for (; q; q --)
	{
		scanf("%d", &n);
		
		if (n%p==0)
		    count=count+1;
	}
	printf("%d",count);
		return 0;
} 

