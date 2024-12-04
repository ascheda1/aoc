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

//138879426

struct row{
	int low, high;
	char c;
	string pass;
};

int main(){
	ifstream infile("in.txt");

	vector<int> data;
	int num;

	while(infile >> num){
		data.push_back(num);
	}

	int wrong_num;
	// for (int i = 25; i < data.size(); i++){
	// 	bool possible = false;
	// 	for (int j = i - 25; j < i; j++){
	// 		for (int k = j + 1; k < i; k++){
	// 			if (data[j] + data[k] == data[i]){
	// 				possible = true;
	// 				goto ende;
	// 			}
	// 		}
	// 	}
	// 	ende:
	// 	if (!possible){
	// 		wrong_num = data[i];
	// 		break;
	// 	}
	// }
	int res = 138879426;
	int max = 0;
	int min = res;
	for (int i = 0; i < data.size(); i++){
		for (int j = i + 1; j < data.size(); j++){
			int sum = 0;
			for (int k = i; k < j; k++){
				sum += data[k];
			}
			if (sum == res){
				for (int k = i; k < j; k++){
					//cout << data[k] << endl;
					if (data[k] > max)
						max = data[k];
					if (data[k] < min){
						min = data[k];
					}
				}
				goto end;
			}
		}
	}
	end:
	cout << max + min << endl;

	return 0;
}
