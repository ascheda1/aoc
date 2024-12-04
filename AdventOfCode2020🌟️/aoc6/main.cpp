#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

int main(){
	ifstream infile("in.txt");
	string str;
	int sum = 0;
	list<char> l;
	bool first = true;
	while (getline(infile, str)){
		list<char> temp_l;
		for (char c : str){
			if (first){
				l.push_back(c);
				temp_l.push_back(c);
			}
			else if (find(l.begin(), l.end(), c) != l.end()){
				temp_l.push_back(c);
			}
		}
		first = false;
		if (!str.empty())
			l = temp_l;

		if (str.empty()){
			sum += l.size();
			l.clear();
			first = true;
		}
	}
	cout << sum << endl;
	return 0;
}
