#include <iostream>

using namespace std;

int main() {
    int age = 20;
    double height = 1.81;
    char letter = 'G';
    string name = "Gustavo";
    int x = 12, y = 8;
    int sum = x + y;
    const double pi = 3.1415926535;

    // cout << age << endl;
    // cout << height << endl;
    // cout << sum << endl;

    cout << fixed;
    cout.precision(8);
    cout << pi << endl;
    return 0;
}