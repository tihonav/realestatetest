// g++ -o test test.cpp 
// g++ -o -std=c++11 test test.cpp 


// TEMPLATE TESTS
#include <vector>
#include <iostream>
#include <algorithm>

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





// MACRO
#define TEST(x,y) void wow(int x, int y)


TEST(a1,b2)
{
	std::cout<<"huest"<< a1 <<"  "<<  b2 <<"!\n";
}







// STRUCTURE CONSTRUCTORS
struct a
{
	int i;
	a(int i1)
	{
		i = i1;
	}
	a(const a &  a1){i = a1.i -1;}
	a& operator=(const a &  a1){i = a1.i + 1; return *this;}
	
};

// LAMBDA EXPRESSIONS
void is_lower(char c )
{
	if(islower(c)) cout<<"Lower: "<<c<<endl;
}

void test_lambda() 
{
	//char s[]="Hello World!";
	auto s="Hello World!";
	int Uppercase = 0; //modified by the lambda
	for_each(s, s+sizeof(s), [&Uppercase] (char c) {
		if (isupper(c))
		Uppercase++;
	});
	cout<< Uppercase<<" uppercase letters in: "<< s<<endl;
	for_each(s, s+sizeof(s), is_lower); 
	for_each(s, s+sizeof(s), [](char a){if(islower(a)) cout<<"Lower2: "<<a<<endl;}); 
	auto  test_func = [](int x, int  y){ return x+y; } ;
	//auto glambda = [](auto a, auto&& b) { return a < b; };// NOT ALLOWED IN C++11
}


int main()
{
	
	// Templates
	C<int> aaaa(100);
	cout<<"Test: "<<endl;
	aaaa.f();


	// structure constructors
	std::cout << "Hello World! " << std::endl;
	a test(1);
	a test2  = test;
	std::cout << test2.i << std::endl;

	// macro
	wow(100,200);

	// lambda
	cout<<"\n\n\n";
	test_lambda();

	// decltype
	vector<int> vec;
	typedef decltype (vec.begin()) CIT;
	for(CIT i=vec.begin(); i!=vec.end(); ++i){}

	// brace initialization
	int arr1[]  = {1,2,3,4}; // the same
	int arr2[4] = {1,2,3,4}; // the same
	int arr3[9] = {1,2,3,4}; // the same
	vector<string> arr4 = {"one","two","three"};
	for(auto i=arr4.begin();i!=arr4.end();i++){cout<<(*i);}; cout<<endl; 
	for_each(arr3, arr3 + sizeof(arr3), [](int i) {cout<<i;}); cout<<endl; 

	return 0;
}
