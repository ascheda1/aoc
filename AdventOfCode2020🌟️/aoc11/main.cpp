#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <sstream>
#include <queue>
#include <list>
#include <algorithm>
#include "omp.h"

using namespace std;

// 97x97 big
// 10x10 small

struct row{
	int low, high;
	char c;
	string pass;
};

enum seat_state{free_seat, occupied_seat, outofgrid_seat};

bool same_fields(vector<vector<char>> a, vector<vector<char>> b){
	for (int i = 0; i < a.size(); i++){
		for (int j = 0; j < a[0].size(); j++){
			if (a[i][j] != b[i][j])
				return false;
		}
	}
	return true;
}

void print_grid(vector<vector<char>> grid){
	for (int i = 0; i < grid.size(); i++){
		for (int j = 0; j < grid[0].size(); j++){
			cout << grid[i][j];
		}
		cout << endl;
	}
}


seat_state occupied(vector<vector<char>> field, int i, int j){
	if (i < 0 || i >= field.size() || j < 0 || j >= field[0].size() || field[i][j] == 'L'){
		return outofgrid_seat;
	}
	if (field[i][j] == '.'){
		return free_seat;
	}
	return occupied_seat;
}
int main(){

	ifstream infile("in.txt");
	string str;
	vector<vector<char>> field;

	while(getline(infile, str)){
		stringstream stream(str);
		vector<char> row;
		char pos;
		while (stream >> pos){
			row.push_back(pos);
		}
		field.push_back(row);
	}

	vector<vector<char>> new_field = field;

	vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1},
									{1, 1}, {-1, -1}, {1, -1}, {-1, 1}};
	bool changing = true;
	while (changing){
		changing = false;
		#pragma omp parallel for
		for (int i = 0; i < field.size(); i++){
			for (int j = 0; j < field[0].size(); j++){
				if (field[i][j] == 'L'){
					for (auto dir : dirs){
						int i_advanced = i, j_advanced = j;
						while (true){
							i_advanced += dir.first;
							j_advanced += dir.second;
							seat_state st = occupied(field, i_advanced, j_advanced);
							if (st == occupied_seat)
							 	goto ende;
							else if (st == outofgrid_seat)
								break;
						}
					}
					new_field[i][j] = '#';
					changing = true;
				}
				else if(field[i][j] == '#'){
					int occ_seats = 0;
					for (auto dir : dirs){
						int i_advanced = i, j_advanced = j;
						while (true){
							i_advanced += dir.first;
							j_advanced += dir.second;
							seat_state st = occupied(field, i_advanced, j_advanced);
							if (st == occupied_seat){
								occ_seats++;
								break;
							}
							else if (st == outofgrid_seat)
								break;
						}
					}

					if (occ_seats >= 5){
						new_field[i][j] = 'L';
						changing = true;
					}
				}
				else
					new_field[i][j] = '.';

				ende:
				true == true;
			}
		}
		//print_grid(new_field);
		field = new_field;
	}

	int occupied_seats = 0;
	for (int i = 0; i < field.size(); i++){
		for (int j = 0; j < field[0].size(); j++){
			if (field[i][j] == '#'){
				occupied_seats++;
			}
		}
	}
	cout << occupied_seats << endl;
	return 0;
}
