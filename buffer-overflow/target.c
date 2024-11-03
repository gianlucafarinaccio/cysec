#include <stdio.h>

void f();

int main(int argc, char** argv)
{
	f();
}

void f()
{
	char buffer[5];
	int i;

	printf("input> ");
	fflush(stdout); /*svuota il buffer*/
	scanf("%s", buffer);
	i=0;

	while ( buffer[i]!=0 )
	{
		fputc(buffer[i], stdout);
		i++;
	}
	printf("\n");

	printf("%p\n", &buffer[0]);
	printf("%p\n", &buffer[4]);
}