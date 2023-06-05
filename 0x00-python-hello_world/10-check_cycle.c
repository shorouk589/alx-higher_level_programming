#include "lists.h"


/**
 * check_cycle - checks linkeds lists containssss a cycles
 * @list: linked lists to checks
 *
 * Return: 1 if the lists has a cycles, 0 if it doesn'tt
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)

		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
