#include "lists.h"

listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to the address of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 *
 * Tim helped with this task
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *reverse;
	listint_t *current = *head;

	if (head != NULL)
	{
		while (fast && fast->next)
		{
			slow = slow->next;
			fast = fast->next->next;
		}
		reverse = reverse_listint(&slow);

		while (reverse)
		{
			if (current->n != reverse->n)
				return (0);
			current = current->next;
			reverse = reverse->next;
		}
	}
	return (1);
}

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: double pointer
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = *head;
	listint_t *next = *head;
	listint_t *reverse = NULL;

	while (prev)
	{
		next = next->next;
		prev->next = reverse;

		reverse = prev;
		prev = next;
	}
	return (reverse);
}
