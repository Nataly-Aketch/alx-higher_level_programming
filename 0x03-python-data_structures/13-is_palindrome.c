#include "lists.h"
/**
 * compare_list - compares two lists
 * @head1: first linked list
 * @head2: second linked list
 * Return: 1 if they're the same,, 0 otherwise
 */
int compare_list(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1, *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n != temp2->n)
		{
			return (0);
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	return (1);
}
/**
 * reverse - reverses a linked list
 * @head: linked list to be reversed
 * Return: reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *new = NULL;

	while (current)
	{
		new = current->next;
		current->next = prev;
		prev = current;
		current = new;
	}
	*head = prev;
	return (prev);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: linked list
 * Return: 1 if found 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *last, *slow = *head, *fast = *head;
	int count = 0, flag = 0;

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		count++;
	}
	if (count == 0 || count == 1)
		flag = 1;
	else
	{
		while (fast && fast->next)
		{
			fast = fast->next->next;
			slow = slow->next;
		}
		last = reverse(&slow);
		if (compare_list(*head, last) == 1)
			flag = 1;
		else
			flag = 0;
	}
	return (flag);
}
