#include <iostream>
#include <vector>
#include <utility>

using namespace std;

void BubbleSort(vector<int>& A) {
    int n = A.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (A[j] < A[j + 1]) {
                swap(A[j], A[j + 1]);
            }
        }
    }
}

int main() {
    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }

    BubbleSort(A);

    for (size_t i = 0; i < A.size(); i++) {
        cout << A[i] << (i == A.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
