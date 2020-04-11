#pragma once
#include <string>



class Job {
	int duration, deadline, profit;
	std::string name;
	double prof_ratio;
public:
	Job(int d, int dead, int p, std::string n) :name(n), duration(d),
		deadline(dead), profit(p), prof_ratio(p / d) {}

	bool operator>(const Job& rhs) {
		return prof_ratio > rhs.prof_ratio;
	}
	bool operator<(const Job& rhs) {
		return prof_ratio < rhs.prof_ratio;
	}

	int getDeadline() {
		return deadline;
	}
	std::string getName() const {
		return name;
	}
	double getRatio() const {
		return prof_ratio;
	}
};