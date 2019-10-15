#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    vector<int> V(25), C(25);

    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> V[i];
    }
    for (int i = 0; i < n; i++){
        cin >> C[i];
    }
    int tmp, total=0;
    for (int i = 0; i < n; i++){
        tmp = (V[i] - C[i]);
        if (tmp >= 0){
            total += tmp;
        }
    }
    cout << total;

    return 0;
}