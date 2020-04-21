#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <numeric>
#include <sstream>
#include <random>
using namespace std;

random_device e;
uniform_int_distribution<> id(1, 1000);
int count = 0;
//vector<int> s{ 8,17,4,2,7 ,15,9,23,32,43 };
vector<int> s;
int target = 0;
//int target = 104;
struct Node {
    Node* left;
    Node* right;
    int sum;
    int remainder;
    vector<int>::iterator next;
    Node(Node* l = nullptr, Node* r = nullptr,int s=0,int _r=0)
        :left(l), right(r), sum(s), remainder(_r) {
        ::count++;
    }
};
void backtrack(Node*& t, string path, string& solution) {
    if (solution.size() > 0)return;
    if (t->next != s.end()) {
            if (t->sum + *t->next == target) {
                solution = path + "," + to_string(*t->next);
                return;
            }
            t->left = new Node;
            t->left->sum = t->sum + *t->next;
            t->left->next = t->next + 1;
            t->left->remainder = t->remainder - *t->next;
            t->right = new Node;
            t->right->sum = t->sum;
            t->right->next = t->next + 1;
            t->right->remainder = t->remainder - *t->next;
            backtrack(t->left, path + "," + to_string(*t->next), solution);

            backtrack(t->right, path, solution);
    }
}

void bb(Node* &t,string path,string& solution) {
    if (solution.size()>0)return;
    if (t->next != s.end()) {
        if (t->sum + *t->next == target) {
            solution = path + "," + to_string(*t->next);
            return;
        }
        if (t->sum + t->remainder < target)return;
        t->left = new Node;
        t->left->sum = t->sum + *t->next;
        t->left->next = t->next + 1;
        t->left->remainder = t->remainder - *t->next;
        t->right = new Node;
        t->right->sum = t->sum;
        t->right->next = t->next + 1;
        t->right->remainder = t->remainder - *t->next;
        if (t->left->sum < target)
            bb(t->left, path + "," + to_string(*t->next), solution);

        bb(t->right, path, solution);
    }
}
int main()
{//do 10 trials
    for (int k = 0; k < 10; k++) {
        s.clear();
        ::count = 0;
        cout << " Trial " << k << endl;
        cout << "--------------------------\n";
        int set_size = 20;
        for (int i = 0; i < set_size; i++)
            s.push_back(id(e));
        target = id(e);
        for (auto x : s)
            cout << x << ",";
        cout << "target =" << target << endl;
        Node* root;
        string solution = "";

        {root = new Node;
        root->remainder = std::accumulate(s.begin(), s.end(), 0);
        root->sum = 0;
        root->next = s.begin();
        bb(root, "", solution);

        int total{ 0 };
        if (solution.size() > 0) {

            string val;
            istringstream iss = istringstream(solution);
            solution[0] = '[';
            solution = solution + ']';
            cout << "bb solution is-> " << solution << endl;
            while (getline(iss, val, ','))
                total += atoi(val.c_str());
        }
        cout << "nodes created bb->" << ::count << endl;
        if (total != 0 && total != target)cout << "error\n";
        }

        {
            root = new Node;
            ::count = 0;
            solution = "";
            root->remainder = std::accumulate(s.begin(), s.end(), 0);
            root->sum = 0;
            root->next = s.begin();
            backtrack(root, "", solution);
            if (solution.size() > 0) {
                solution[0] = '[';
                solution = solution + ']';
                cout << "backtracking solution is-> " << solution << endl;
            }
            cout << "nodes created backtracking->" << ::count << endl;
        }
        cout << "--------------------------\n";

    }

}

