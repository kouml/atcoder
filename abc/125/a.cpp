#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int a, b, t;
    cin >> a >> b >> t;

    int i = 0;
    while (true){
        t = t - a;
        if (t < 0){
            break;
        }
        i += 1;
    }
    cout << i*b;

    return 0;
}
