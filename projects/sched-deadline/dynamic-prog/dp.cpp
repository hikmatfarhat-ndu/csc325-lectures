
#include <algorithm>
#include <iostream>
#include <vector>
#include <list>
#include <string>

// Must define DP below  to select
// the proper operators < and >
// Must be done BEFORE including Job.h

#define DP
#include "Job.h"
Matrix<int> solve (std::vector<Job>& jobs) {

    std::sort(std::begin(jobs), std::end(jobs));
    int max_deadline =
        (jobs.end() - 1)->deadline();
    int n = 5;
    Matrix<int> opt(n + 1, max_deadline + 1);
    for (int i = 0; i <= max_deadline; i++)
        opt[0][i] = 0;

    for (int i = 1; i <= n; i++) {//number of jobs included
        for (int t = 0; t <= max_deadline; t++) {
            int tp = std::min(jobs[i - 1].deadline(), t)
                - jobs[i - 1].duration();
            if (tp < 0) {
                opt[i][t] = opt[i - 1][t];
            }
            else {
                opt[i][t] = std::max(opt[i - 1][t],
                    jobs[i - 1].profit() + opt[i - 1][tp]);
            }

        }
    }    
    return opt;
}
int main() {
    Matrix<int> solution;
    Job A{ 1,2, 100, "A" };
    Job B(1, 1, 19, "B");
    Job C(1, 2, 27, "C");
    Job D(1, 1, 25, "D");
    Job E(1, 3, 15, "E");
    std::vector<Job> jobs{ A,B,C,D,E };
    solution=solve(jobs);
    for (int i = 0; i <solution.rows(); i++) {
        for (int j = 0;j<solution.cols(); j++) {
            std::cout << solution[i][j] << ",";
        }
        std::cout << std::endl;
    }
}