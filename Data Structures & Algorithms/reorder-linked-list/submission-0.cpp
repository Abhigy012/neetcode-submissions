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

ListNode* revList(ListNode* head) {
    if (!(head && head->next)) {
        return head;
    }
    ListNode* p = NULL;
    ListNode* q = head;
    ListNode* r = head->next;

    while (q) {
        q->next = p;
        p = q;
        q = r;
        if (r) r = r->next;
    }
    return p;
}

int lenList(ListNode* head){
    int l = 0;
    ListNode* temp = head;
    while(temp){
        l += 1;
        temp = temp->next;
    }
    return l;
}

class Solution {
   public:
    void reorderList(ListNode* head) {
        if(!head || !head->next){
            return;
        }
        int l = lenList(head);
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = NULL;
        while(fast && fast->next){
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        prev->next = NULL;
        ListNode* newStart = revList(slow);
        ListNode* dummy = new ListNode(-1);
        ListNode* temp = dummy;
        ListNode* t1 = head;
        ListNode* t2 = newStart;
        while(t1 && t2){
            temp->next = t1;
            temp = temp->next;
            t1 = t1->next;
            temp->next = t2;
            temp = temp->next;
            t2 = t2->next;
        }
        if(t1){
            temp->next = t1;
            temp = temp->next;
            t1 = t1->next;
        }
        if(t2){
            temp->next = t2;
            temp = temp->next;
            t2 = t2->next;
        }
    }
};
