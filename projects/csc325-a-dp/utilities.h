#pragma once
#include <string>
#include <vector>

template <typename T>
class Matrix {
private:
	T** p;
	int rows, cols;
public:
	Matrix(int n, int m) :rows(n), cols(m) {
		/* not the most efficient way
		   but it is easy and most of the time
		   we do it once */
		p = new T * [n];
		for (int i = 0;i < n;i++) {
			p[i] = new T[m]();//initialize to 0
		}
	}
	T* operator[](int i) {
		return p[i];
	}
	int getRows() {
		return rows;
	}
	int getCols() {
		return cols;
	}
};

std::vector<int> convert(std::vector<std::string>& sv);
Matrix<double>  sequence_al(std::string, std::string);
std::vector<std::string> split(const std::string& s, char delimiter);
Matrix<bool> subset_sum(const std::vector<int>& A, const int S);
std::vector<int> ss_sol(Matrix<bool>& m,std::vector<int>& A, const int S);
