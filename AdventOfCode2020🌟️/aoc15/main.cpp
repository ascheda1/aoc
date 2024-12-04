#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <sstream>
#include <queue>
#include <list>
#include <algorithm>
#include <cmath>
#include <limits.h>
#include <bits/stdc++.h>
#include <omp.h>
#include <cstddef>

using namespace std;

void print_vector(vector<int> v){
	for (auto e : v){
		cout << e << endl;
	}
}

int main(){
	ifstream infile("in.txt");

	int num;
	vector<int> line;
	map<int, vector<int>> s;

	int i = 0;
	while (infile >> num){
		//line.push_back(num);
		vector<int> v = {i};
		s.insert({num, v});
		i++;
	}
	for (; i < 30000000; i++){ //30000000
		if (i % 100000 == 0) cout << i << endl;
		auto it = s.find(num);
		if (it->second.size() > 1){

			//cout << it->second[it->second.size() - 1] << " " << it->second[it->second.size() - 2] << endl;
			num = it->second[it->second.size() - 1] - it->second[it->second.size() - 2];
		}
		else{
			num = 0;
		}

		auto it_new = s.find(num);
		if (it_new != s.end()){
			it_new->second.push_back(i);
		}
		else{
			vector<int> v = {i};
			s.insert({num, v});
		}
		//cout << num << endl;
	}

	cout << num << endl;
	return 0;
}
