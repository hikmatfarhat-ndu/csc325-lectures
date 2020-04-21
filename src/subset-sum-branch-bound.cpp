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
    if (t != nullptr) {
        //std::cout << "Node sum= " << t->sum << " remainder= "
          //  << t->remainder << " next= " << (t->next==s.end()?0:*t->next) << std::endl;
        if (t->next != s.end()) {
            if (t->sum + *t->next == target) {
                cout << path + "," + to_string(*t->next) << " is the solution\n";
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
    else return;
}

void bb(Node* &t,string path,string& solution) {
    if (solution.size()>0)return;
    if (t != nullptr) {
        //std::cout << "Node sum= " << t->sum << " remainder= "
          //  << t->remainder << " next= " << (t->next==s.end()?0:*t->next) << std::endl;
        if (t->next != s.end()) {
            if (t->sum + *t->next == target) {
                cout << path+","+to_string(*t->next)<< " is the solution\n";
                solution = path + "," + to_string(*t->next);
                return;
            }
            if (t->sum + t->remainder <target)return;
            t->left = new Node;
            t->left->sum = t->sum + *t->next;
            t->left->next = t->next + 1;
            t->left->remainder = t->remainder - *t->next;
            t->right = new Node;
            t->right->sum = t->sum;
            t->right->next = t->next + 1;
            t->right->remainder = t->remainder - *t->next;
            if (t->left->sum< target)
                bb(t->left,path+","+to_string(*t->next),solution);
            
            bb(t->right,path,solution);
        }
    }
    else return;
}
int main()
{
    int set_size = 20;
    for (int i = 0; i < set_size; i++)
        s.push_back(id(e));
    target = id(e);
    for (auto x : s)
        cout << x << ",";
    /*s = { 4,12,18,22,100,200,300,4};
    target = 17;*/
    cout << "target =" << target << endl;
    Node* root;
    string solution = "";

    {root  = new Node;
    root->remainder = std::accumulate(s.begin(), s.end(), 0);
    root->sum = 0;
    root->next = s.begin();
    bb(root, "", solution);
    string val;
    istringstream iss = istringstream(solution);
    int total{ 0 };
    while (getline(iss, val, ','))
        total += atoi(val.c_str());

    cout << "number= " << ::count << endl;
    if (total!=0 && total != target)cout << "error\n";
    }
    
    {
        root = new Node;
        ::count = 0;
        solution = "";
        root->remainder = std::accumulate(s.begin(), s.end(), 0);
        root->sum = 0;
        root->next = s.begin();
        backtrack(root, "", solution);
        cout << "number= " << ::count << endl;
    }

}

