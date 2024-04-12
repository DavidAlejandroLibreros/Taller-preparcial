#include <iostream>
using namespace std;

int main(){

for (int i = 1; i <= 5; i++){
    for(int j = 5; j > i; j--){
        cout << " ";

    }
    for(int k =1 ; k <= (2 * i - 1); k++) {
        cout << "*";
    }
    cout << endl;
}

for (int i = 5 - 1; 1 < i; i--){
    for(int j = 1; j < i; j++){
        cout << " ";

    }
    for(int k = 1;  k <=(2 * (5 - 1)) ; k++){
        cout << "*";


    }
    cout << endl;


}
}