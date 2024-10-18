#include <bits/stdc++.h>
using namespace std;

void printMat(int degseq[], int n)
{
	int mat[n][n];
	memset(mat, 0, sizeof(mat));

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (degseq[i] > 0 && degseq[j] > 0) {
				degseq[i]--;
				degseq[j]--;
				mat[i][j] = 1;
				mat[j][i] = 1;
			}
		}
	}

	cout << "\n"
		<< setw(3) << "	 ";
	for (int i = 0; i < n; i++)
		cout << setw(3) << "(" << i << ")";
	cout << "\n\n";
	for (int i = 0; i < n; i++) {
		cout << setw(4) << "(" << i << ")";
		for (int j = 0; j < n; j++)
			cout << setw(5) << mat[i][j];
		cout << "\n";
	}
}
int main()
{
	int degseq[] = { 2, 2, 1, 1, 1 };
	int n = sizeof(degseq) / sizeof(degseq[0]);
	printMat(degseq, n);
	return 0;
}

