// Rotate an array by k postions using normal method

#include <iostream>
using namespace std;

void arrayRotate(int arr[], int n, int k) {
    for(int i = 0; i < k; i++) {
        int temp = arr[n - 1];
        for (int j = n - 1; j > 0; j--) {
            arr[j] = arr[j - 1];
        }
        arr[0] = temp;
    }
}
int main() {
    int arr[] = {1, 2, 3, 4, 5, 6};
    int n = 6;
    int k = 3;
    
    arrayRotate(arr, n, k); // 4 5 6 1 2 3
    for (int i = 0; i < n; i++ ) {
        cout << arr[i] << " ";
    }
    return 0;
}

// Time Complexity = O(k * n)
// Space Complexity = ?