// Revesre individual words in a string

#include <iostream>
using namespace std;

string reverseWord(string s, int start, int end) {
    while (start < end) {
        char temp = s[start];
        s[start++] = s[end];
        s[end--] = temp;
    }
    return s;
}

string reverseWordsInSentence(string s) {
    int n = s.length();
    int i = 0, start = 0, end;
    while (s[i] != '\0') {
        if (s[i] == ' ') {
            end = i - 1;
            s = reverseWord(s, start, end);
            start = i + 1;
        }
        i++;
    }
    s = reverseWord(s, start, n - 1);
    return s;
}

int main() {
    string s = "I ma tihcrA dohtaR"; // I am Archit Rathod
    cout << reverseWordsInSentence(s);
    return 0;
}