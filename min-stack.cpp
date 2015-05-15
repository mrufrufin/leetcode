class MinStack {
private:
    stack<int> myStack;
    stack<int> minStack;
public:
    void push(int x) {
        if(myStack.empty() || x <= minStack.top()){

            minStack.push(x);
            
        };
        myStack.push(x);
    }

    void pop() {
        if(myStack.top() == minStack.top()){
          minStack.pop();  
            
        };
        myStack.pop();
        
    }

    int top() {
        return myStack.top();
    }

    int getMin() {
        return minStack.top();
    }
};
