// g++ -o test test.cpp 

#include <vector>
#include <iostream>

using namespace std;

template<class K>
class C {
    struct P {
		int i;
		P(int j){i=j;}
	};
	vector<P> vec;
public:	
	C(int b){vec.push_back(P(10));}
	void f();
	vector<int> vec2;
};

template<class K> void C<K>::f() {
	typename vector<P>::iterator p = vec.begin();

	//vector<P>::iterator p = vec.begin();
	vector<int>::iterator p1 = vec2.begin();
	cout<<(*p).i<<endl;
}

int main()
{
	
	C<int> a(100);
	cout<<"Test: "<<endl;
	a.f();
	return 0;
}
