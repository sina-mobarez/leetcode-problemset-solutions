l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    first_number = ""
    second_number = ""
    for i in reversed(l1):
        first_number += str(i)
    for i in reversed(l2):
        second_number += str(i)
    return list(reversed(list(map(int, str(int(first_number) + int(second_number))))))


print(addTwoNumbers(l1, l2))