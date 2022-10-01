#include <iostream>
using namespace std;

template <typename T>
class BinaryTreeNode {
public:
    T data;
    BinaryTreeNode* left;
    BinaryTreeNode* right;

    BinaryTreeNode(T data) {
        this -> data = data;
        left = NULL;
        right = NULL;
    }

    ~BinaryTreeNode() {
        delete left;
        delete right;
    }
};

template <typename T>
BinaryTreeNode<T>* takeInputLevelWise() {
    cout << "Enter root data: ";
    T rootData;
    cin >> rootData;
    if(rootData == -1)
        return NULL;
    BinaryTreeNode<T>* root = new BinaryTreeNode<T>(rootData);
    queue<BinaryTreeNode<T>*> q;
    q.push(root);
    while(q.size() != 0) {
        BinaryTreeNode<T>* front = q.front();
        q.pop();
        T leftData;
        cout << "Enter left child of " << front -> data << ": ";
        cin >> leftData;
        if(leftData != -1) {
            BinaryTreeNode<T>* child = new BinaryTreeNode<T>(leftData);
            front -> left = child;
            q.push(child);
        }
        T rightData;
        cout << "Enter right child of " << front -> data << ": ";
        cin >> rightData;
        if(rightData != -1) {
            BinaryTreeNode<T>* child = new BinaryTreeNode<T>(rightData);
            front -> right = child;
            q.push(child);
        }
    }
    cout << endl;
    return root;
}

template <typename T>
void printTreeLevelWise(BinaryTreeNode<T>* root) {
    if(root == NULL) 
        return;
    queue<BinaryTreeNode<T>*> q;
    q.push(root);
    while(q.size() != 0) {
        BinaryTreeNode<T>* front = q.front();
        q.pop();
        cout << front -> data << ": ";
        if(front -> left != NULL) {
            cout << "L" << front -> left -> data << " ";
            q.push(front -> left);
        }
        if(front -> right != NULL) {
            cout << "R" << front -> right -> data;
            q.push(front -> right);
        }
        cout << endl;
    }
}

void mirrorBinaryTree(BinaryTreeNode<int>* root) {
    if(root == NULL) 
        return;
    BinaryTreeNode<int>* temp = root -> left;
    root -> left = root -> right;
    root -> right = temp;
    mirrorBinaryTree(root -> left);
    mirrorBinaryTree(root -> right);
}

int main() {
    BinaryTreeNode<int>* root = takeInputLevelWise<int>();
    mirrorBinaryTree(root);
    printTreeLevelWise(root);
}
