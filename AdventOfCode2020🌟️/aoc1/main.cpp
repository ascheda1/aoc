#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	ifstream infile("in.txt");
	int n;
	vector<int> numbers;
	while (infile >> n){
		numbers.push_back(n);
	}

	for(int i = 0; i < numbers.size(); i++){
		for (int j = i + 1; j < numbers.size(); j++){
			for (int k = j + 1; k < numbers.size(); k++){
				if (numbers[i] + numbers[j] + numbers[k] == 2020){
					cout << numbers[i] * numbers[j] * numbers[k] << endl;
					return 0;
				}
			}
		}
	}
}
