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
//#include <bits/stdc++.h>
#include <omp.h>
#include <cstddef>

using namespace std;

void print_vector(vector<int> v){
	for (auto e : v){
		cout << e << endl;
	}
}

struct interval{
	int min, max;
};

struct {
	bool operator() (interval a, interval b){
		return a.min < b.min;
	}
}Compare;

struct col{
	vector<int> data;
	int num;
};

struct {
	bool operator() (col a, col b){
		return a.data.size() < b.data.size();
	}
}Compare_size;


int main(){
	ifstream infile("in.txt");

	string line;
	vector<interval> intervals;
	while(getline(infile, line)){

		if (line.empty()){
			break;
		}
		string sub_line = line.substr(line.find(": ") + 2, line.length());
		stringstream stream_line(sub_line);

		interval i1;
		interval i2;
		char h; //help
		string or_s;
		stream_line >> i1.min >> h >> i1.max >> or_s >> i2.min >> h >> i2.max;
		intervals.push_back(i1);
		intervals.push_back(i2);
	}
	vector<interval> original_intervals = intervals;
	sort(intervals.begin(), intervals.end(), Compare);

	vector<interval> ints_uni;

	for (auto e : intervals){
		if (ints_uni.empty() || e.min - 1 > ints_uni[ints_uni.size() - 1].max){
			ints_uni.push_back(e);
			continue;
		}
		else{
			ints_uni[ints_uni.size() - 1].max = e.max;
		}
	}

	while (getline(infile, line)){
		if (line.compare("your ticket:") == 0){
			break;
		}
	}
	getline(infile, line);

	stringstream stream_line(line);
	vector<int> my_ticket;
	while(getline(stream_line, line, ',')){
		int num = stoi(line);
		my_ticket.push_back(num);
	}


	while (getline(infile, line)){
		if (line.compare("nearby tickets:") == 0)
			break;
	}

	long result = 0;
	vector<vector<int>> tickets;
	while (getline(infile, line)){
		if (line.empty())
			break;
		stringstream stream_line(line);
		vector<int> ticket;
		bool ticket_ok = true;
		while(getline(stream_line, line, ',')){
			int num = stoi(line);
			ticket.push_back(num);
			bool ok = false;
			for (auto e : ints_uni){
				if (num >= e.min && num <= e.max){
					ok = true;
					break;
				}
			}
			if (!ok){
				ticket_ok = false;
				result += num;
			}
		}
		if (ticket_ok){
			tickets.push_back(ticket);
		}
	}
	cout << "RESULT_1: " << result << endl;

	vector<col> cols;

	for (int i = 0; i < my_ticket.size(); i++){
		col c;
		c.num = i;
		cols.push_back(c);
	}

	for (int j = 0; j < original_intervals.size(); j += 2){
		interval i1 = original_intervals[j];
		interval i2 = original_intervals[j + 1];
		//bool correct_int = true;
		int i = 0;
		//vector<int> available_intervals;
		for (; i < my_ticket.size(); i++){
			bool correct_int = true;

			for (vector<int> ticket : tickets){
				if (ticket[i] < i1.min || (ticket[i] > i1.max && ticket[i] < i2.min) || ticket[i] > i2.max){
					correct_int = false;
					break;
				}
			}
			if (correct_int){
				cols[i].data.push_back(j/2);
				//break;
			}
		}
		//cols.push_back(available_intervals);
	}
	vector<int> ints_assigned(my_ticket.size());

	sort(cols.begin(), cols.end(), Compare_size);

	for (int i = 0; i < cols.size(); i++){
		vector<int> c = cols[i].data;
		ints_assigned[cols[i].num] = c[0];
		cout << c[0] << " ";
		for (int j = i + 1; j < cols.size(); j++){
			auto it = find(cols[j].data.begin(), cols[j].data.end(), c[0]);
			if (it != cols[j].data.end())
				cols[j].data.erase(it);
		}
	}
	cout << endl;

	long long result_2 = 1;
	for (int i = 0; i < ints_assigned.size(); i++){
		if (ints_assigned[i] >= 0 && 5 >= ints_assigned[i]){
			cout << my_ticket[i] << " INTERVAL: " << original_intervals[2 * ints_assigned[i]].min << " - " <<original_intervals[2 * ints_assigned[i]].max <<
			" " << original_intervals[2 * ints_assigned[i] + 1].min << " - " << original_intervals[2 * ints_assigned[i] + 1].max << endl;
			result_2 *= my_ticket[i];
		}
	}
	cout << endl;
	cout << "RESULT_2: " << result_2 << endl;
	return 0;
}
