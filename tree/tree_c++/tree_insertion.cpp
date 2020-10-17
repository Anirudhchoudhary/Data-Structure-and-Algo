#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
};

void deleteDeepest(Node *root, Node *d_node)
{
    queue<Node *> q;
    q.push(root);
    Node *temp = NULL;
    while (!q.empty())
    {
        temp = q.front();
        q.pop();
        if (temp == d_node)
        {
            temp = NULL;
            delete (d_node);
            return;
        }

        if (temp->right)
        {
            if (temp->right == d_node)
            {
                temp->right = NULL;
                delete (d_node);
                return;
            }
            else
                q.push(temp->right);
        }

        if (temp->left)
        {
            if (temp->left == d_node)
            {
                temp->left = NULL;
                delete (d_node);
                return;
            }
            else
                q.push(temp->left);
        }
    }
}

Node *deletetion(Node *root, int key)
{
    if (root == NULL)
    {
        return NULL;
    }

    if (root->left == NULL and root->right == NULL)
    {
        if (root->data == key)
        {
            return NULL;
        }
        else
            return root;
    }

    queue<Node *> q;
    q.push(root);
    Node *temp = NULL;
    Node *key_node = NULL;
    while (!q.empty())
    {
        temp = q.front();
        q.pop();
        if (temp->data == key)
        {
            key_node = temp;
        }
        if (temp->left)
        {
            q.push(temp->left);
        }

        if (temp->right)
        {
            q.push(temp->right);
        }
    }

    if (key_node != NULL)
    {
        int x = temp->data;
        deleteDeepest(root, temp);
        key_node->data = x;
    }

    return root;
}

Node *CreateNode(int data)
{
    Node *newNode = new Node();
    if (!newNode)
    {
        cout << "Memory Usage Error";
        return NULL;
    }

    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

Node *insertNode(Node *root, int data)
{
    if (root == NULL)
    {
        root = CreateNode(data);
        return root;
    }

    queue<Node *> q;
    q.push(root);

    while (!q.empty())
    {
        Node *temp = q.front();
        q.pop();

        if (temp->left != NULL)
        {
            q.push(temp->left);
        }
        else
        {
            temp->left = CreateNode(data);
            return root;
        }

        if (temp->right != NULL)
        {
            q.push(temp->right);
        }
        else
        {
            temp->right = CreateNode(data);
            return root;
        }
    }
}

void inorder(Node *temp)
{
    if (temp == NULL)
    {
        return;
    }

    inorder(temp->left);
    cout << temp->data << " ";
    inorder(temp->right);
}

int main()
{
    Node *root = CreateNode(10);
    root->left = CreateNode(11);
    root->left->left = CreateNode(7);
    root->right = CreateNode(9);
    root->right->left = CreateNode(15);
    root->right->right = CreateNode(8);

    cout << "Inorder traversal before insertion: ";
    inorder(root);
    cout << endl;

    int key = 12;
    root = insertNode(root, key);

    cout << "Inorder traversal after insertion: ";
    inorder(root);
    cout << endl;

    key = 9;
    deletetion(root, key);
    cout << "Inorder traversal after deletion: ";
    inorder(root);
    cout << endl;

    return 0;
}