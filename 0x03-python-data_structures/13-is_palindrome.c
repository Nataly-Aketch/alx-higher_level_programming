#include "lists.h"
/**
 * search - searches a for a node
 * @head: head node
 * @idx: index to be searched
 * Return: node if found, NULL otherwise
 */
listint_t *search(listint_t *head, unsigned int idx)
{
	unsigned int count = 0;

	while (head && idx > count)
	{
		head = head->next;
		count++;
	}
	return (head);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: linked list
 * Return: 1 if found 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *last, *first;
	int count = 0, flag = 0, sec_count;

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		count++;
	}
	if (count == 0)
		flag = 1;
	else
	{
		sec_count = count - 1;
		first = *head;
		last = search(*head, sec_count);
		while (first && last != first)
		{
			if (first->n == last->n)
				flag = 1;
			sec_count--;
			last = search(first, sec_count);
			first = first->next;
		}
	}
	return (flag);
}
