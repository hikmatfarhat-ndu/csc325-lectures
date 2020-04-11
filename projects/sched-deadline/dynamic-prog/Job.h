#pragma once
#include <string>
#include <vector>

using namespace std;

template <typename T>
class Matrix {
private:
	T* p;
	int _rows, _cols;
public:
	Matrix(int n=2, int m=2) :_rows(n), _cols(m) {
		/* more efficient to create
			a 1-d array that represents
			a 2-d matrix
			*/
		p = new T[n * m]();
	}
	//copy constructor
	Matrix(const Matrix& rhs) {		
		_rows = rhs._rows;
		_cols = rhs._cols;
		p = new T[_rows * _cols];
		for (int i = 0; i < _rows * _cols; i++)
			p[i] = rhs.p[i];

	}
	Matrix& operator=(const Matrix& rhs) {
		_rows = rhs._rows;
		_cols = rhs._cols;
		delete[] p;
		p = new T[_rows * _cols];
		for (int i = 0; i < _rows * _cols; i++)
			p[i] = rhs.p[i];
		return *this;
	}
	T* operator[](int i) {
		return &p[i * _cols];
	}
	int rows() const {
		return _rows;
	}
	int cols() const {
		return _cols;
	}
	
	
};

class Job {
	int _start,_duration, _deadline, _profit;
	std::string _name;
	int _previous = -1;
	double prof_ratio;
public:
	Job(int dur, int dead, int p, std::string n) :
		_name(n), _duration(dur),_deadline(dead), _profit(p),
		prof_ratio(p / dur),_start(-1) {
		
	}
	//operators need to be constant
	//otherwise std::less will complain
#ifdef DP
	bool operator>(const Job& rhs) const{
		return _deadline > rhs._deadline;
	}
	bool operator<(const Job& rhs) const{
		return _deadline < rhs._deadline;
	}
#endif // DP
#ifdef GREEDY
	bool operator>(const Job& rhs) const {
		return prof_ratio > rhs.prof_ratio;
	}
	bool operator<(const Job& rhs) const {
		return prof_ratio < rhs.prof_ratio;
	}
#endif // GREEDY

	int profit() const {
		return _profit;
	}
	int deadline () const {
		return _deadline;
	}
	std::string name() const {
		return _name;
	}
	double ratio() const {
		return prof_ratio;
	}
	bool overlap(const Job& rhs) {
		if (_start+_duration <= rhs._start)
			return true;
		if (rhs._start+rhs._duration<= _start)
			return true;
		
		//otherwise
		return false;

	}
	int duration() const {
		return _duration;
	}
	
};