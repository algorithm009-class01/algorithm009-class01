/*
21. 合并两个有序链表

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* result;
        if(l1)
        {
            result=l1;
        }else
        {
            return l2;
        }
		ListNode* tail=result;
         if(l2&&l1->val >= l2->val)
		   {
		       tail=l2;
               l2=l2->next;
			   tail->next=l1;
			   result=tail;
		   }

        while(l2)
		{
		   if(l1&&l1->val >= l2->val)
		   {
		       tail->next=l2;
			   tail=l2;
               l2=l2->next;
               tail->next=l1;
               if(l2==NULL)
               {
                   break;
               }
		   }
           else
           {
               if(l1->next==NULL)
               {
                   l1->next=l2;
                   break;
               }
               tail=l1;
               l1=l1->next;
           }
		}
		return result;
    }
};
