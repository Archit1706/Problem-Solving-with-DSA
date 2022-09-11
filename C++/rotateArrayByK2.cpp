// Rotate an array by K positions using array reversal method 

#include <iostream>
using namespace std;

void reverseArray(int arr[], int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start++] = arr[end];
        arr[end--] = temp;
    }
}

void arrayRotate(int arr[], int n, int k) {
    reverseArray(arr, 0, n - k - 1);
    reverseArray(arr, n - k, n - 1);
    reverseArray(arr, 0, n - 1);
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

// Time Complexity = O(n)
// Space Complexity = ?