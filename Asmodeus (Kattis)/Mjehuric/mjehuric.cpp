#include<bits/stdc++.h>
using namespace std;

void printArr(int arr[], int n){
    for (int i=0;i<n;i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

void bubble(int arr[], int n){
    int swaps = 1, temp;
    while (swaps){
        swaps = 0;
        for (int i=0;i<n-1;i++){
            if (arr[i] > arr[i+1]){
                temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                swaps = 1;
                printArr(arr, n);
            }
        }
    }
}

int main(void){
    int n = 5;
    int arr[n];
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }
    bubble(arr, n);
    return 0;.
}
