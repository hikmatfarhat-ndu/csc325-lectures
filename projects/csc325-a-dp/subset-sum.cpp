#include <vector>
#include "utilities.h"

Matrix<bool> subset_sum(const std::vector<int>& A, const int S) {
	int n = A.size();
	Matrix<bool> T(n + 1, S + 1);
	for (int j = 0;j <= S;j++) {// no solution when using 0 items
		T[0][j] = false;
	}
	for (int i = 0;i <= n;i++) {//always a solution when sum=0
		T[i][0] = true;
	}

	for (int i = 1;i <= n;i++) {
		for (int j = 1;j <= S;j++) {
			if (A[i - 1] <= j)
				T[i][j] = T[i - 1][j] || T[i - 1][j - A[i - 1]];
			else T[i][j] = T[i - 1][j];
		}
	}
	return T;
}

std::vector<int> ss_sol(Matrix<bool>& m,std::vector<int>& A,const int sum){
	int i=A.size();
	int s=sum;
	std::vector<int> sol;
	while(i>0 && s>0){
	//check if element n is in the solution
		bool v = m[i - 1][s - A[i - 1]];
  	if(s>=A[i-1]&& m[i-1][s-A[i-1]]){
		sol.push_back(A[i-1]);
		//continue at m[i-1][s-A[i-1]]
		s=s-A[i-1];
		i=i-1;
	}
	else {
		// A[i-1] not in the solution
		// continue at m[i-1][s]
		i=i-1;
	}
	}
	return sol;
  }
