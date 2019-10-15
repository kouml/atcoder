#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b){
    if (b == 0){
        return abs(a);
    }
    return gcd(b, a%b);
}

int gcd_wrapper(int a, int b){
    return gcd(max(a,b), min(a,b));
}

int main(){
    int n;
    vector<int> A((1e+5)+10);
    vector<int> L((1e+5)+10);
    vector<int> R((1e+5)+10);
    vector<int> M((1e+5)+10);

    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> A[i];
    }

    L[0] = 0;
    for (int i=0;i < (n-1);i++){
        L[i+1] = gcd_wrapper(L[i], A[i]);
    }

    R[n+1] = 0;
    for (int i=n;0 < i;i--){
        R[i] = gcd_wrapper(R[i+1], A[i]);
    }

    int max_v = -1;
    for (int i=0;i<(n-1);i++){
        M[i] = gcd_wrapper(L[i], R[i + 1]);
        max_v = max(M[i], max_v);
    }

    cout << max_v;
    return 0;
}