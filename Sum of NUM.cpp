#include <iostream>
using namespace std;

int main() {
	int t,n,d=0;
	cin>>t;
	while(t--){
		cin>>n;
		while(n>0){
		d=d+(n%10);
		n=n/10;}
		cout<<d<<endl;
		d=0;
		
		
		
	}
	return 0;
}