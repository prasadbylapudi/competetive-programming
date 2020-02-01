
#include <bits/stdc++.h> 

using namespace std;

int main() {
    
    int n;
    std::cin >> n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
       std::cin >>arr[i];
    }
    sort(arr,arr+n);
    
    
	for(int i=0;i<n;i++)
	{
	    std::cout << arr[i] << std::endl;
	}
	return 0;
}
