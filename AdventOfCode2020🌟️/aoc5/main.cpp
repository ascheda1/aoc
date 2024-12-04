#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

struct row{
	int low, high;
	char c;
	string pass;
};

int main(){
	ifstream infile("in.txt");
	vector<int> l;
	vector<int>::iterator it = l.begin();

	int max_id = 0, id, r, c, bot, top;
	string data;
	while (getline(infile, data)){
		bot = 0;
		top = 127;
		for (int i = 0; i < 6; i++){
			if (data[i] == 'F')
				top = bot + (top - bot) / 2;
			else
				bot = top - (top - bot) / 2;
		}
		if (data[6] == 'F')
			r = bot;
		else
			r = top;

		bot = 0;
		top = 7;
		for (int i = 7; i < 9; i++){
			if (data[i] == 'L')
				top = bot + (top - bot) / 2;
			else
				bot = top - (top - bot) / 2;
			//cout << bot << " " << top << endl;
		}
		if (data[9] == 'L')
			c = bot;
		else
			c = top;
		id = r * 8 + c;

		l.push_back(id);

		if (id > max_id)
			max_id = id;
	}

	sort(l.begin(), l.end());

	for (int i = 0; i < l.size(); i++){
		if (l.at(i) + 1 != l.at(i + 1)){
			cout <<l.at(i) + 1 << endl;
			return 0;
		}
	}

	// while (true){
	// 	for (int i : l){
	// 		it = find(l.begin(), l.end(), )
	// 	}
	// }
	//cout << max_id << endl;
	return 0;
}
