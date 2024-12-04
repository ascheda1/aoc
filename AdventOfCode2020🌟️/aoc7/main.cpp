#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <sstream>
#include <queue>
#include <list>
#include <algorithm>

using namespace std;

struct row{
	string bag;
	vector<pair<string, int>> subbags;
};

vector<row> rows;

int rec(string bag){

	for (row r : rows){
		if (r.bag.compare(bag) == 0){
			int sum = 0;
			for (pair<string, int> sub : r.subbags){
				sum += sub.second + sub.second * rec(sub.first);
			}
			return sum;
		}
	}
}

int main(){
	ifstream infile("in.txt");
	string line;


	while (getline(infile, line)){
		row r;
		r.bag = line.substr(0, line.find(" bags contain "));
		//cout << r.bag << endl;
		string other_bags = line.substr(line.find(" bags contain ") + 13, line.length());

		stringstream stream(other_bags);
		string temp_s;
		while(getline(stream, temp_s, ',')){
			string num = temp_s.substr(1,2);
			if (num.compare("no") == 0){
				break;
			}
			string bag = temp_s.substr(3, temp_s.find(" bag") - 3);
			r.subbags.push_back({bag, stoi(num)});
			//cout << bag << endl;
		}

		rows.push_back(r);
	}

	int sum = rec("shiny gold");

	// queue<string> q;
	// list<string> l;
	// q.push("shiny gold");
	// while(!q.empty()){
	// 	string main_bag = q.front();
	// 	q.pop();
	// 	for (row r : rows){
	// 		for (pair<string,int> bag : r.subbags){
	// 			if (bag.first.compare(main_bag) == 0){
	// 				if (find(l.begin(), l.end(), r.bag) == l.end()){
	// 					l.push_back(r.bag);
	// 					q.push(r.bag);
	// 				}
	// 				break;
	// 			}
	// 		}
	// 	}
	// }
	cout << sum << endl;
	return 0;
}
