#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n,rem=0,sum=0;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    while(n)
    {
        rem=n%10;
        sum+=rem;
        n/=10;
    }
    printf("%d",sum);
    return 0;
}


