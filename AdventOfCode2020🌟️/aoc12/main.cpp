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

using namespace std;

struct row{
	char command;
	int num;
};

enum e{east = 0, south = 1, west = 2, north = 3};

int main(){
	ifstream infile("in.txt");

	string str;
	int east = 0, south = 0;
	pair<int,int> waypoint = {10, -1};
	while(getline(infile, str)){
		stringstream stream(str);
		row r;
		stream >> r.command;
		stream >> r.num;

		if (r.command == 'N'){
			//south -= r.num;
			waypoint.second -= r.num;
		}
		else if (r.command == 'S'){
			//south += r.num;
			waypoint.second += r.num;
		}
		else if (r.command == 'E'){
			//east += r.num;
			waypoint.first += r.num;
		}
		else if (r.command == 'W'){
			//east -= r.num;
			waypoint.first -= r.num;
		}
		else if (r.command == 'L'){
			float angle = -r.num * M_PI / 180;
			pair<int,int> new_wayp = {round(cos(angle) * waypoint.first - sin(angle) * waypoint.second),
									round(sin(angle) * waypoint.first + cos(angle) * waypoint.second)};
			waypoint = new_wayp;
		}
		else if (r.command == 'R'){
			float angle = r.num * M_PI / 180;
			pair<int,int> new_wayp = {round(cos(angle) * waypoint.first - sin(angle) * waypoint.second),
									round(sin(angle) * waypoint.first + cos(angle) * waypoint.second)};
			waypoint = new_wayp;
		}
		else if (r.command == 'F'){
			east += r.num * waypoint.first;
			south += r.num * waypoint.second;
		}
	}

	cout << abs(east) + abs(south) << endl;

	return 0;
}
