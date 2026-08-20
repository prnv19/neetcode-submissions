/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummy = new ListNode();
        ListNode* d = dummy;
        ListNode* cur = head;
        ListNode* group_start = head;
        int i = 0;

        while (cur != nullptr) {
            i++;
            if (i == k) {
                ListNode* next_grp = cur->next;
                cur->next = nullptr;

                ListNode* new_head = reverse(group_start);

                d->next = new_head;
                group_start->next = next_grp;
                d = group_start;

                cur = next_grp;
                group_start = next_grp;
                i = 0;
            } else {
                cur = cur->next;
            }
        }
        return dummy->next;
    }

private:
    ListNode* reverse(ListNode* node){
        ListNode* prev = nullptr;
        ListNode* temp;
        while (node != nullptr){
            temp = node->next;
            node->next = prev;
            prev = node;
            node = temp;
        }
        return prev;
    }
};
