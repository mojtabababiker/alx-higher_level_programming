#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a new node in a sorted linked_list depinding
 * @head: pointer to the first node on the sorted linked_list
 * @number: new node value
 * Return: new node address or NULL in fialure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *slow_node = NULL, *fast_node = NULL, *new_node = NULL;
	listint_t *temp = NULL;
	/* Allocate the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	/* Creat the new node */
	new_node->next = NULL;
	new_node->n = number;
	/* if the linked list is empty */
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	/*searching for the node that have a number larger than the new node n*/
	temp = *head;
	if (((*head)->n) > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	/* using the two pointer approch */
	while (*head != NULL)
	{
		slow_node = *head;
		fast_node = slow_node->next;
		if (fast_node == NULL || fast_node->n > number)
		{
			/* inser the new node before this node */
			new_node->next = fast_node;
			slow_node->next = new_node;
			*head = temp;
			return (new_node);
		}
		*head = (*head)->next;
	}
	*head = temp;
	return (NULL);
}
