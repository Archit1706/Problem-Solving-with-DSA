#include <iostream>
using namespace std;

int isAlphabet(char ch) {
    return ((ch >= 'A' && ch <= 'a') || (ch >= 'a' && ch <= 'z'));
}

string reverse (string s) {
    int start = 0;
    int end = s.length();

    while (start < end) { 
        if (!isAlphabet(s[start])) 
            start++;

        else if (!isAlphabet(s[end]))
            end--;
        
        else {
            char temp = s[start];
            s[start++] = s[end];
            s[end--] = temp;
        }
    }
    return s;
}

int main() {
             // this#can$be;a%mixed(:string!
    string s = "gnir#tsd$ex;i%maebn(:acsiht!";
    cout << reverse(s);
    return 0;
}