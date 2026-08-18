/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> hashmap;
        Node* cur = head;
        while (cur != nullptr){
            hashmap[cur] = new Node(cur->val);
            cur = cur->next;
        }
        Node* dummy = new Node(-1);
        cur = dummy;
        while (head != nullptr){
            cur->next = hashmap[head];
            if (head->random == nullptr) cur->next->random = nullptr;
            if (head-> random != nullptr) cur->next->random = hashmap[head->random];

            cur = cur->next;
            head = head->next;
        }
        return dummy->next;
    }
};
