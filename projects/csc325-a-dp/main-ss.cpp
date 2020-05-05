// sequence-alignment.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

/* solution to the sequence alignment problem
using dynamic programming 

*/
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <random>
#include "utilities.h"
using namespace std;
std::pair<vector<int>,int>
getSS() {

	ifstream input;
	string SA;
	input.open("ss-input.txt");
	input >> SA;
	vector<string> va = split(SA, ',');
	int S;
	input >> S;
	input.close();
	vector<int> A = convert(va);
	return std::pair<vector<int>,int>(A, S);
}
int main()
{
	//auto [A, S] = getSS();
	std::vector<int> A;
	std::random_device e;
	std::uniform_int_distribution id(1, 50);
	for (int i = 0; i < 20; ++i) {
		A.push_back(id(e));
	}
	int S = id(e);
	Matrix<bool> V = subset_sum(A, S);
	/*for (int i = 0;i<V.getRows();i++) {
		for (int j = 0;j < V.getCols();j++) {
			std::cout << V[i][j] << ",";
		}
		std::cout << std::endl;
	}*/
	std::cout << "Set \n";
	for (auto& x : A) {
		std::cout << x << ",";
	}
	std::cout << "| " << S << endl;
	std::cout << "-------------\n";
	if (V[A.size()][S] == true) {
		vector<int> sss = ss_sol(V, A, S);
		for (auto& x : sss) {
			std::cout << x << ",";
		}
		std::cout << std::endl;
	}
	else {
		std::cout << "No solution\n";
	}
}
