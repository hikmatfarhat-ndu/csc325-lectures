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
