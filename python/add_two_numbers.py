# leetcode 2
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            curr.next = ListNode(val % 10)
            curr = curr.next

            carry = val // 10

        #if carry > 0:
        #    curr.next = ListNode(carry)
        return dummy.next

    def insert(self, root, item):
        temp = ListNode(0)
        temp.val = item
        temp.next = root
        root = temp
        return root

    def display(self, root):
        new_arr = []
        while root is not None:
            #print(root.val)
            new_arr.append(root.val)
            root = root.next
        print(new_arr)

    def array2List(self, arr, n):
        root = None
        for i in range(n-1, -1, -1):
            root = self.insert(root, arr[i])
        return root

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    arr2 = [2, 3, 9]
    n = len(arr)
    n2 = len(arr2)

    s = Solution()
    l1 = s.array2List(arr, n)
    l2 = s.array2List(arr2, n2)
    r = s.addTwoNumbers(l1, l2)
    s.display(r)
