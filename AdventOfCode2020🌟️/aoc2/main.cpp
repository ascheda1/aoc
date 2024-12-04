#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct row{
	int low, high;
	char c;
	string pass;
};

int main(){
	ifstream infile("in.txt");

	vector<row> data;
	row r;
	while (infile >> r.low >> r.c >> r.high >> r.c){
		getline(infile, r.pass);
		//cout  << r.low << r.c << r.high << r.c << r.pass << endl;
		data.push_back(r);
	}
	int pass_counter = 0;
	for (row ro : data){
		int word_counter = 0;
		if (ro.pass.at(ro.low + 1) == ro.c){
			word_counter++;
		}
		if (ro.pass.at(ro.high + 1) == ro.c){
			word_counter++;
		}

		if (word_counter == 1){
			pass_counter++;
		}
	}
	cout << pass_counter << endl;
	return 0;
}
