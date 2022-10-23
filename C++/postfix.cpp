#include <iostream>
#include <stack>
#include <math.h>
using namespace std;
bool isOperand(char t)
{
    if (t >= '0' && t <= '9')
        return true;
    else
        return false;
}
bool isOperator(char t)
{
    switch (t)
    {
    case '+':
    case '-':
    case '/':
    case '*':
    case '^':
        return true;
    }
    return false;
}
int evaluatePostfixExpression(string postfix)
{
    stack<int> stk;
    char token;

    for (int i = 0; i < postfix.length(); ++i)
    {
        token = postfix[i];
        if (isOperand(token))
        {
            stk.push(token - '0');
        }
        else if (isOperator(token))
        {

            int v1, v2;
            v1 = stk.top();
            stk.pop();
            v2 = stk.top();
            stk.pop();

            switch (token)
            {
            case '+':
                stk.push(v2 + v1);
                break;
            case '-':
                stk.push(v2 - v1);
                break;
            case '*':
                stk.push(v2 * v1);
                break;
            case '/':
                stk.push(v2 / v1);
                break;
            case '^':
                stk.push(pow(v2, v1));
                break;
            }
        }
    }
    return stk.top();
}
int main()
{
    string postfix;
    cout << "Enter Postfix Expression: ";
    cin >> postfix;
    cout << "The result is: " << evaluatePostfixExpression(postfix) << endl;
}