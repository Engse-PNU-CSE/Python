#include <iostream>

using namespace std;

int main()
{
    int x, y, i, array[10000];
    cin >> x >> y;
    for(i = 0; i < x; i++) {
        cin>>array[i];
        if(array[i] < y) cout<<array[i];
        if(i < x-1) cout<<" ";
    }
    return 0;
}