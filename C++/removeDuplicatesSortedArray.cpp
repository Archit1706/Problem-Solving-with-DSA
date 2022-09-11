// remove duplicates from a sorted array

#include <iostream>
using namespace std;

int removeDuplicates(int arr[], int n) {
    if (n == 0 || n == 1) {
        return n;
    }
    int len = 0, i;
    for (i = 0; i < n - 1; i++) {
        if (arr[i] != arr[i + 1]) {
            arr[len++] = arr[i];
        }
    }
    arr[len++] = arr[n - 1];
    return len;
}

int main() {
    int arr[] = {1,1,1,1,3,3,3,3,6,6,6,8,8,9,10};
    int n = 15;
    cout << removeDuplicates(arr, n) << endl; // arr[] = {1, 3, 6, 8, 9, 10}, len = 6
    return 0;
}

// Time Complexity = O(n)
// Space Complexity = O(n)