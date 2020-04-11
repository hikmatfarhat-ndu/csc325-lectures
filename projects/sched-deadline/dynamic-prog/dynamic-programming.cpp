
#include <algorithm>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include "Job.h"


int main() {

    Job A{1,2, 100, "A" };
    Job B(1, 1, 19, "B");
    Job C(1, 2, 27, "C");
    Job D(1, 1, 25, "D");
    Job E(1, 3, 15, "E");

    std::vector<Job> jobs{ A,B,C,D,E };
    std::sort(std::begin(jobs), std::end(jobs));
    int max_deadline = (jobs.end() - 1)->deadline();
    int n = 5;
    Matrix<int> opt(n+1, max_deadline + 1);
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
    for (int i = 0; i <= n; i++) {
        for (int t = 0; t <= max_deadline; t++) {
            std::cout << opt[i][t] << ",";
        }
        std::cout << std::endl;
    }
}