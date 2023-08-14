#include "lists.h"

listint_t *check_palindrome(listint_t **head, listint_t *tail);
/**
 * is_palindrome - Check a singly linked_list if it's a palindrome
* @head: Address of the pointer of the first node in the singly linked_list
* Return: 1 if the linked_list is a palindrome or 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	listint_t *result, *temp;
	/* Empty list and a list which contians only one elements */
	/* booth are palindrome, so no need for check */
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	result =  check_palindrome(head, *head);
	*head = temp;
	if (result != NULL)
		return (1);
	return (0);
}

/**
 * check_palindrome - a recursive function checks if the given
 *                    singly linked list is a palindrome or not
 * @head: a pointer to the first node in the linked list
 * @tail: a pointer to the last node
 * Return: listint_t pointer if the head->n == tial->n, NULL other wise
 */

listint_t *check_palindrome(listint_t **head, listint_t *tail)
{

	/* the Base Case that we reach the last node in the linked_list */
	if (tail->next == NULL)
	{
		/*if the postion in right side == the same postion in left*/
		if ((*head)->n == tail->n)
			return ((*head)->next);
		return (NULL); /*else*/
	}
	/* recall the function with same head and the next node of tail */
	*head = check_palindrome(head, tail->next);
	if (*head != NULL)
	{
		if ((*head)->n == tail->n)
		{
			if ((*head)->next == NULL)
				return (*head);

			return ((*head)->next);

		return (NULL);
		}
	}
	return (NULL);
}
