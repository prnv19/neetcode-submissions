class MinStack {
private:
vector<int> stk, min_stack;
public:
    MinStack() {}
    
    void push(int val) {
        stk.push_back(val);
        if(min_stack.empty() || val < min_stack.back()){
            min_stack.push_back(val);
        }
        else{
            min_stack.push_back(min_stack.back());
        }
    }
    
    void pop() {
        stk.pop_back();
        min_stack.pop_back();
    }
    
    int top() {
        return stk.back();
    }
    
    int getMin() {
        return min_stack.back();
    }
};
