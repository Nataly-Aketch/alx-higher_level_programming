#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 1 if there is 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	while (head)
	{
		if (!list)
			return (0);
		if (head->next == list)
			return (1);
		head = head->next;
	}
	return (0);
}
