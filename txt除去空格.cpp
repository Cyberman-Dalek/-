#include<iostream>

#include<fstream>

#include<string>

using namespace std;

int main()

{

	ifstream in("1.txt", ios::in);

	ofstream out("2.txt", ios::out);

	string str;

	while(in&&in>>str)

	{

		out<<str;

	}

	return 0;

}
