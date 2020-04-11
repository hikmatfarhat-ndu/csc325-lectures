// scheduling-deadline.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <tuple>
#include <queue>
#include <functional>
//Must define GREEDY below to select
//the proper operators for < and >
// Must be done BEFORE including Job.h

#define GREEDY
#include "../dynamic-prog/Job.h"
int max_deadline(const std::vector<Job> & jobs) {
	int _max_deadline = 0;
	for (auto itr = jobs.begin(); itr != jobs.end()
		; itr++)
		if (itr -> deadline() > _max_deadline)
			_max_deadline = itr->deadline();

	return _max_deadline;
}
std::vector<std::string> 
	solve(const std::vector<Job> & jobs) {

	std::vector<std::string> solution;
	std::vector<bool> 
		slot(max_deadline(jobs), false);

	std::priority_queue<Job> q;
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
int main()
{	
	std::vector<std::string> s;
	Job A(1, 2, 100, "A");
	Job B(1, 1, 190, "B");
	Job C(1, 2, 27, "C");
	Job D(1, 1, 25, "D");
	Job E(1, 3, 15, "E");
	std::vector<Job> jobs{ A,B,C,D,E };
	s = solve(jobs);
	for (auto l : s) {
		std::cout << l << std::endl;
	}
	
}
	

