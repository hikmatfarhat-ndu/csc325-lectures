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

#include "utilities.h"
using namespace std;



//int main()
//{
//	ifstream input;
//	input.open("sa-input.txt");
//	string both;
//	input >>both;
//	input.close();
//	vector<string> r = split(both, ',');
//	/* input sequences */
//	string X = r[0];
//	string Y = r[1];
//	
//	
//
//	Matrix<double> T = sequence_al(X, Y);
//	/* print the optimal values */
//	for (int i = 0;i < T.getRows();i++) {
//		for (int j = 0;j < T.getCols();j++) {
//			cout << T[i][j] << ",";
//		}
//		cout << endl;
//	}
//	string SA;
//	input.open("ss-input.txt");
//	input >> SA;
//	vector<string> va = split(SA, ',');
//	int S;
//	input >> S;
//	input.close();
//	vector<int> A = convert(va);
//	
//	Matrix<bool> V = subset_sum(A, S);
//	for (int i = 0;i<V.getRows();i++) {
//		for (int j = 0;j < V.getCols();j++) {
//			std::cout << V[i][j] << ",";
//		}
//		std::cout << std::endl;
//	}
//	vector<int> sss=ss_sol(V,A,S);
//
//}
