/* ch5 if_else.c */

#include <stdio.h>
#include <stdlib.h>

int main()
	{
	char ch;

	printf("Play again ? [Y/y] ");
	scanf("%c", &ch);

	if ((ch == 'y') || (ch == 'Y'))
		{
		printf("Play again !\n");
		printf("I like this game...\n");
		}
	else
		{
		printf("Exit the game !\n");
		printf("I do'nt like this game.\n");
		}
	printf("Test over !\n");

	system("PAUSE");
	return 0;
	}

