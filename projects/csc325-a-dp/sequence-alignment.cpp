#include <string>
#include <algorithm>
#include<vector>
#include <sstream>
#include "utilities.h"




Matrix<double>  sequence_al(std::string X, std::string Y) {
	/* alpha=cost of mistmatch */
	double alpha = 0.6;
	/* alpha_gap=cost of a gap */
	double alpha_gap = 0.5;
	double cost;
	/* length of the input sequences */
	int n = X.length();
	int m = Y.length();
	/* solution, i.e the optimal value NOT the actual solution*/
	Matrix<double> T(n + 1, m + 1);
	/* initialization */
	for (int i = 0;i <= n;i++)
		T[i][0] = alpha_gap * i;
	for (int j = 0;j <= m;j++)
		T[0][j] = alpha_gap * j;
	/* recursive formula, bottom up */
	for (int i = 1;i <= n;i++) {
		for (int j = 1;j <= m;j++) {
			if (X[i - 1] == Y[j - 1])cost = 0;
			else cost = alpha;
			T[i][j] = std::min(cost + T[i - 1][j - 1], std::min(alpha_gap + T[i][j - 1],
				alpha_gap + T[i - 1][j]));
		}
	}
	return T;

}