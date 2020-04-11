
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <fstream>
#include <sstream>
#include "Job.h"
int max_deadline(const std::vector<Job>& jobs) {
	int _max_deadline = 0;
	for (auto itr = jobs.begin(); itr != jobs.end()
		; itr++)
		if (itr->deadline() > _max_deadline)
			_max_deadline = itr->deadline();

	return _max_deadline;
}
std::vector<std::string>
greedy_solve(const std::vector<Job>& jobs) {

	std::vector<std::string> solution;
	std::vector<bool>
		slot(max_deadline(jobs), false);

	std::priority_queue<Job, std::vector<Job>, greedy_less> q;
	for (auto itr = jobs.begin();
		itr != jobs.end(); itr++)
		q.push(*itr);

	while (!q.empty()) {
		auto j = q.top();
		for (int sl = j.deadline(); sl > 0; sl--) {
			if (slot[sl - 1] == false) {
				slot[sl - 1] = true;
				solution.push_back(j.name());
				break;
			}
		}
		q.pop();
	}
	return solution;
}


Matrix<int> dp_solve(std::vector<Job>& jobs) {

	std::sort(std::begin(jobs), std::end(jobs), dp_less());
	int max_deadline =
		(jobs.end() - 1)->deadline();
	//int n = 5;
	Matrix<int> opt(jobs.size() + 1, max_deadline + 1);
	for (int i = 0; i <= max_deadline; i++)
		opt[0][i] = 0;

	for (int i = 1; i <= jobs.size(); i++) {//number of jobs included
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
	std::ifstream ifs;
	std::string instr;
	ifs.open("jobs.txt");
	std::vector<Job> jobs;

	while (std::getline(ifs, instr)) {
		instr.erase(std::remove(instr.begin(),
			instr.end(), ' '), instr.end());
		if (instr.find('#') != std::string::npos || instr.size() == 0)
			continue;

		jobs.push_back(read_job(instr));
	}
	
	Matrix<int> solution;
	solution = dp_solve(jobs);
	for (int i = 0; i < solution.rows(); i++) {
		for (int j = 0; j < solution.cols(); j++) {
			std::cout << solution[i][j] << ",";
		}
		std::cout << std::endl;
	}
	std::vector<std::string> greedy_sol;
	greedy_sol = greedy_solve(jobs);
	auto itr = greedy_sol.begin();
	for (; itr != greedy_sol.end()-1; itr++)
		std::cout << *itr << ",";
	//skip the comma for the last item
	itr = greedy_sol.end() - 1;
	std::cout << *itr << std::endl;


}