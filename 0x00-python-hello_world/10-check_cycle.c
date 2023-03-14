#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 1 if there is 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast && slow)
	{
		if (fast->next == slow)
			return (1);
		if (fast == slow)
			return (0);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
