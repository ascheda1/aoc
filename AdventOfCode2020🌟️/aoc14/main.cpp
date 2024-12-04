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

using namespace std;

struct row{
	string left;
	string right;
};

enum e{east = 0, south = 1, west = 2, north = 3};

vector<string> memory_adresses;
void recursive_fill(string mask){
	string mask_copy0 = mask;
	string mask_copy1 = mask;
	bool found = false;
	for (int i = 0; i < mask.length(); i++){
		if (mask[i] == 'X'){
			mask_copy0[i] = '0';
			mask_copy1[i] = '1';
			recursive_fill(mask_copy0);
			recursive_fill(mask_copy1);
			return;
		}
	}
	if (!found){
		memory_adresses.push_back(mask);
		return;
	}
}

int main(){
	ifstream infile("in.txt");

	string mask;

	vector<pair<int, unsigned long long>> memory;

	while (true){
		string line;
		getline(infile, line);
		row r;
		if (line.empty())
			goto empty;
		r.left = line.substr(0, line.find(" ="));
		r.right = line.substr(line.find("= ") + 2, line.length());

		if (r.left.compare("mask") == 0){
			mask = r.right;
			//cout << mask << endl;
		}
		else{
			int mem_index = stoi(r.left.substr(4, r.left.find("]")));
			int mem_value = stoi(r.right);

			bitset<36> mem_bit(mem_index);
			string bit_memory = mem_bit.to_string();
			for (int i = 0; i < mask.length(); i++){
				if (mask[i] == '0')
					bit_memory[i] = mask[i];
				else if (mask[i] == '1')
					bit_memory[i] = '1';
				else if (mask[i] == 'X')
					bit_memory[i] = 'X';
			}


			recursive_fill(bit_memory);

			for (auto addr : memory_adresses){
				bool already_in = false;
				for (int i = 0; i < memory.size(); i++){
					if (memory[i].first == bitset<36>(addr).to_ulong()){
						memory[i].second = mem_value;
						//cout << bitset<36>(bit_memory).to_ulong() << endl;
						already_in = true;
						break;
					}
				}
				if (!already_in){
					memory.push_back({bitset<36>(addr).to_ulong(), mem_value});
				}
			}

			memory_adresses.clear();


			// //cout << bit_memory << endl;
			// for (int i = 0; i < memory.size(); i++){
			// 	if (memory[i].first == mem_index){
			// 		memory[i].second = bitset<36>(bit_memory).to_ulong();
			// 		//cout << bitset<36>(bit_memory).to_ulong() << endl;
			// 		goto empty;
			// 	}
			// }
			// memory.push_back({mem_index, bitset<36>(bit_memory).to_ulong()});
			// //cout << bitset<36>(bit_memory).to_ulong() << endl;

		}

		empty:
		if (line.empty())
			break;
	}

	unsigned long long result = 0;
	for (int i = 0; i < memory.size(); i++){
		result += memory[i].second;
	}
	cout << result << endl;
	return 0;
}
