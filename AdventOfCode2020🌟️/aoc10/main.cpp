#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct jolt{
	int val;
	int possible_cons = 0;
	long precounted = -1;
};
vector<jolt> jolts;

long rec(int i){
	if (i == jolts.size() - 1)
		return 1;
	jolt j = jolts[i];
	if (j.precounted != -1)
		return j.precounted;

	long sum = 0;
	for (int k = i + 1; k < i + 1 + j.possible_cons; k++){
		sum += rec(k);
	}
	jolts[i].precounted = sum;
	return sum;
}

bool Compare(jolt a, jolt b){
	return a.val < b.val;
}
int main(){
	ifstream infile("in.txt");
	jolt j;
	j.val = 0;
	jolts.push_back(j);
	while(infile >> j.val){
		jolts.push_back(j);
	}
	sort(jolts.begin(), jolts.end(), Compare);

	j.val = jolts[jolts.size() - 1].val + 3;
	jolts.push_back(j);

	int one_jolts = 0, three_jolts = 0;

	for (int i = 0; i < jolts.size(); i++){
		for (int j = i + 1; j <= i + 3; j++){
			if (j < jolts.size() && jolts[i].val + 3 >= jolts[j].val){
				jolts[i].possible_cons++;
			}
		}
	}
	long res = rec(0);
	cout << res << endl;
	return 0;
}
