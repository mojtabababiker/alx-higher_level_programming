#include "lists.h"

/**
 * check_cycle - check if the geven linked list has a cycle or not
 * @list: the head node of the linked list to check
 * Return: 0 if no cycle found, 1 otherwise
 */
int check_cycle(listint_t *list)
{

	listint_t *slow_ptr = NULL, *fast_ptr = NULL;

	if (list == NULL || list->next == NULL)
		return (0);
	slow_ptr = list;
	fast_ptr = list;
	while (fast_ptr != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next;
		if (fast_ptr == NULL || fast_ptr->next == NULL)
			return (0);
		if (fast_ptr == list || fast_ptr->next == list || fast_ptr->next == slow_ptr)
			return (1);
		fast_ptr = fast_ptr->next;
	}
	return (0);
}
