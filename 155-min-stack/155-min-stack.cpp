class MinStack {
    struct node{
        int data;
        node* prev = nullptr;
        node* next = nullptr;
    };
    node* head;
    node* min;
public:
    MinStack() {
        head = nullptr;
    }
    
    void push(int val) {
        if(head == nullptr){
            head = new node;
            head = new node;
            head -> prev = nullptr;
            head -> data = val;
            head -> next = nullptr;
            min = head;
        }
        else{
            node* temp = new node;
            head -> next = temp;
            temp -> prev = head;
            temp -> data = val;
            temp -> next = nullptr;
            head = head -> next;
            if(min -> data >= val){
                node* tempmin = new node;
                min -> next = tempmin;
                tempmin -> prev = min;
                tempmin -> data = val;
                tempmin -> next = nullptr;
                min = min -> next;
            }
        }
    }
    
    void pop() {
        int val = head -> data;
        if(min -> data == val){
            min = min -> prev;
            // min -> next = 0;
        }
        head = head -> prev;
        // head -> next = nullptr;

        // return data;
    }
    
    int top() {
        return head -> data;
    }
    
    int getMin() {
        return min -> data;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */