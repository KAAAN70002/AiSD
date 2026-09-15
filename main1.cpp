#include <iostream>
#include <vector>
#include <utility>

using namespace std;

void SelectionSort(vector<int>& A) {
    int n = A.size();
    for (int i = 0; i < n; i++) {
        int max_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (A[j] > A[max_idx]) {
                max_idx = j;
            }
        }
        swap(A[i], A[max_idx]);
    }
}

int main() {
    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }

    SelectionSort(A);

    for (size_t i = 0; i < A.size(); i++) {
        cout << A[i] << (i == A.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
