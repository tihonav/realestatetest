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
	char s[]="Hello World!";
	int Uppercase = 0; //modified by the lambda
	for_each(s, s+sizeof(s), [&Uppercase] (char c) {
		if (isupper(c))
		Uppercase++;
	});
	cout<< Uppercase<<" uppercase letters in: "<< s<<endl;
	for_each(s, s+sizeof(s), is_lower); 
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

	return 0;
}
