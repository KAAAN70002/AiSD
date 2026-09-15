#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<int>& A) {
    vector<int> counts(101, 0);
    for (int x : A) {
        counts[x]++;
    }
    
    int idx = 0;
    for (int val = 0; val <= 100; val++) {
        while (counts[val] > 0) {
            A[idx++] = val;
            counts[val]--;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }

    CountSort(A);

    for (size_t i = 0; i < A.size(); i++) {
        cout << A[i] << (i == A.size() - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}
