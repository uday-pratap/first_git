#include<stdio.h>
void sideways(int);
void sideways(int n)
{
    int x,y;
    for (y= 0; y < n; y++)
    {
        for (x= 0; x <= y; x++)
            putchar('*');
        putchar('\n');
    }
    for (y= n-1; y > 0; y--)
    {
        for (x= 0; x < y; x++)
            putchar('*');
        putchar('\n');
    }
}

void main()
{
 int n;
 scanf("%d",&n);
 sideways(n);
}
