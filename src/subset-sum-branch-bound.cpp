#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <numeric>
#include <sstream>
#include <random>
#include <queue>
#include <tuple>
using namespace std;
int returns = 0;
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
    string path;
    vector<int>::iterator next;
    Node(Node* l = nullptr, Node* r = nullptr,int s=0,int _r=0)
        :left(l), right(r), sum(s), remainder(_r),path("") {
        ::count++;
    }
};
void bfs(Node*& t, string& solution) {
    std::queue<Node*> q;
    
    q.push(t);
    while (!q.empty()) {
        Node* c = q.front();
        q.pop();
        if (c->next != s.end()) {
            if (c->sum + *c->next == target) {//found solution. stop
                solution = c->path + "," + to_string(*c->next);
                break;
            }
            if (c->sum + c->remainder < target) {//skip this branch no solution
                continue;
            }
            c->left = new Node;
            c->left->sum = c->sum + *c->next;
            c->left->next = c->next + 1;
            c->left->remainder = c->remainder - *c->next;
            c->left->path = c->path +","+ to_string(*c->next);
            c->right = new Node;
            c->right->sum = c->sum;
            c->right->next = c->next + 1;
            c->right->remainder = c->remainder - *c->next;
            c->right->path = c->path;
            if (c->left->sum < target)
                q.push(c->left);

            q.push(c->right);

        }

    }

}
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
            if (t->left->sum < target)
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
        if (t->sum + t->remainder < target) {
            returns++;
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
        if (t->left->sum < target)
            bb(t->left, path + "," + to_string(*t->next), solution);

        bb(t->right, path, solution);
    }
}
tuple<double, double, double, string, string> student(int id) {
    if (id == 1)return std::make_tuple(78, 45.5, 93, "hikmat", "farhat");
    return make_tuple(44, 45, 89, "John", "Doe");
}

int main()
{//do 20 trials

    for (int k = 0; k < 20; k++) {
        s.clear();
        ::count = 0;
        returns = 0;
        cout << " Trial " << k << endl;
        cout << "--------------------------\n";
        int set_size = 15;
       
        for (int i = 0; i < set_size; i++)
            s.push_back(id(e));
        
        std::sort(s.begin(), s.end(), std::greater<int>());

        //target = 17*id(e);
        //s = { 40,7,3,3,1,1,1,1};
        //for (auto x : s)
          //  cout << x << ",";
        Node* root;
        string solution = "";

        {root = new Node;
        root->remainder = std::accumulate(s.begin(), s.end(), 0);
        target =root->remainder-id(e);
        cout << "target =" << target << endl;
	cout<<"remainder=" <<root->remainder<<endl;
        root->sum = 0;
        root->next = s.begin();
        bb(root, "", solution);

        int total{ 0 };
        if (solution.size() > 0) {

            string val;
            istringstream iss = istringstream(solution);
            solution[0] = '[';
            solution = solution + ']';
            cout << "DFS solution is-> " << solution << endl;
            while (getline(iss, val, ','))
                total += atoi(val.c_str());
        }
        cout << "nodes created DFS->" << ::count << endl;
        cout << "returns= " << returns << endl;
        if (total != 0 && total != target)cout << "error\n";
        }

       /* {
            ::count = 0;
            root = new Node;
            solution = "";
            root->remainder = std::accumulate(s.begin(), s.end(), 0);
            root->sum = 0;
            root->next = s.begin();
            bfs(root, solution);
            if (solution.size() > 0) {
                solution[0] = '[';
                solution = solution + ']';
                cout << "BFS solution is-> " << solution << endl;
            }
            cout << "nodes created BFS->" << ::count << endl;
        }*/
        {
            ::count = 0;
            root = new Node;
            solution = "";
            root->remainder = std::accumulate(s.begin(), s.end(), 0);
            root->sum = 0;
            root->next = s.begin();
            backtrack(root, "", solution);
            
            if (solution.size() > 0) {
                solution[0] = '[';
                solution = solution + ']';
                cout << "backtrack solution is-> " << solution << endl;
            }
            cout << "nodes created backtrack->" << ::count << endl;
        }
        cout << "--------------------------\n";

    }
    auto t = std::make_tuple<int, int>(3, 4);
    auto [exam1, exam2, exam3, first, last] = student(1);
    cout << "exam1 =" << exam1 << endl;
    cout << "exam2 =" << exam2 << endl;
    cout << "exam3 =" << exam3 << endl;
    cout << "first =" << first << endl;
    cout << "last =" <<last << endl;

    
}

