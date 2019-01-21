# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        # 设置一个快指针和慢指针
        # 快指针比满指针快一步遍历
        # 慢指针将快指针遍历好的每一个node的next设置为默认结束node， 比如ListNode(0)
        # 如果存在闭环， 则快指针会遍历到一个node， 它的next是ListNode(0)
        # 否则会正常结束遍历
        # 参考：https://leetcode.com/problems/linked-list-cycle/discuss/220006/Python-time-complexity-O(n)
        
        defaultEndNode = ListNode(0)
        
        node = head
        while node.next:
            if node.next == defaultEndNode:
                return True
            checked = node
            node = node.next
            checked.next = defaultEndNode

        return False
    
    
    # 方法2: 和Solution2一样
    # 用快指针和慢指针。
    # 快指针比慢指针快两步， 遍历链表直到两者相遇
    # 改进点： 如果碰到一个None， 停止遍历
    # 参考： https://leetcode.com/problems/linked-list-cycle/discuss/219146/Python%3A-97-Faster-and-Slower-approach
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
        
#         if not head or not head.next :
#             return False
        
#         faster = head.next
#         slower = head
        
#         while faster and faster.next and faster != slower :
#             faster = faster.next.next
#             slower = slower.next
        
#         return False if not faster or not faster.next else True