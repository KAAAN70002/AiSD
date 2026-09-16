#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

void InsertionSort(vector<int>& A) {
    int n = A.size();
    for (int i = 1; i < n; i++) {
        int key = A[i];
        int j = i - 1;
        while (j >= 0 && A[j] > key) {
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = key;
    }
}

int main() {
    string line;
    getline(cin, line);
    stringstream ss(line);
    
    vector<int> A;
    int x;
    while (ss >> x) {
        A.push_back(x);
    }

    InsertionSort(A);

    for (size_t i = 0; i < A.size(); i++) {
        cout << A[i] << (i == A.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
