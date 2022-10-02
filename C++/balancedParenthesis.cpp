#include <iostream>
using namespace std;
#include <stack>

bool balancedParenthesis(char* str) {
    stack<char> st;
    for(int i=0; str[i] != '\0'; i++) {
        if(str[i] == '(' || str[i] == '{' || str[i] == '[') {
            st.push(str[i]);
        }
        else if(str[i] == ')') {
            if(st.top() != '(') 
                return false;
            st.pop();
        }
        else if(str[i] == '}') {
            if(st.top() != '{') 
                return false;
            st.pop();
        }
        else if(str[i] == ']') {
            if(st.top() != '[') 
                return false;
            st.pop();
        }
    }
    return st.empty();
}

int main() {
    char* str = new char[100];
    cin.getline(str, 100);
    cout << (balancedParenthesis(str) ? "True" : "False");
}
