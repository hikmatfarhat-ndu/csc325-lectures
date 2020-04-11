// scheduling-deadline.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <tuple>
#include <queue>
#include <functional>
#include "Job.h"

bool operator>(const Job& l,const Job & r) {
	return l.getRatio() > r.getRatio();
}
bool operator<(const Job& l, const Job& r) {
	return l.getRatio() < r.getRatio();
}
int main()
{
	std::vector<std::string> list;
	bool slot[] { false,false,false,false,false };
	Job A(1, 2, 100, "A");
	Job B(1, 1, 19, "B");
	Job C(1, 2, 27, "C");
	Job D(1, 1, 25, "D");
	Job E(1, 3, 15, "E");
	std::priority_queue<Job> q;
	q.push(A); q.push(B); q.push(C); q.push(D); q.push(E);
	while (!q.empty()) {
		auto j = q.top();
		for (int sl = j.getDeadline(); sl >0; sl--) {
			if (slot[sl-1] == false) {
				slot[sl-1] = true;
				list.push_back(j.getName());
				break;
			}
		}
		q.pop();
	}
	for (auto l : list) {
		std::cout << l<< std::endl;
	}
}
	

