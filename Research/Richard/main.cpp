#include <iostream>
#include <cmath>

using namespace std;

int main(){
    string operation;
    double number1 = 2, number2 = 1;


    cout << "Enter 1st Number: ";
    cin >> number1;
    cout << "Enter Operation -+/*: ";
    cin >> operation;
    cout << "Enter 2nd Number: ";
    cin >> number2;

    if (operation == "+") {
        cout << number1 + number2;
    } else if (operation == "-") {
        cout << number1 - number2;
    } else if (operation == "/") {
        cout << number1 / number2;
    } else if (operation == "*") {
        cout << number1 * number2;
    } else {
        cout << "Doesn't work, please stick to the given operations";
    }
        


    return 0;
}
