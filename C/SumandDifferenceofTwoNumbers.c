#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int n,m;
    float a,b;
    scanf("%d %d\n%f %f",&n,&m,&a,&b);
    
    printf("%d %d\n%.1f %.1f",n+m,n-m,a+b,a-b);
    
    
    return 0;
}

