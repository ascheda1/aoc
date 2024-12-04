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

using namespace std;

struct row{
	char command;
	int num;
};

enum e{east = 0, south = 1, west = 2, north = 3};


vector<string> split(string str, char delimiter) {
  vector<string> internal;
  stringstream ss(str); // Turn the string into a stream.
  string tok;

  while(getline(ss, tok, delimiter)) {
    internal.push_back(tok);
  }

  return internal;
}

/**
 * Returns least common multiple of two numbers
 * @param a number 1
 * @param b number 2
 * @return lcm(a, b)
 */

 int gcd(int a, int b) {
     if (a < 1 || b < 1) {
         cout << "PROBLEMO" << endl;
		 return 0;
     }
     int remainder = 0;
     do {
         remainder = a % b;
         a = b;
         b = remainder;
     } while (b != 0);
     return a;
 }

int lcm(int a, int b) {
    if (a == 0 || b == 0) {
        return 0;
    }
    return (a * b) / gcd(a, b);
}

/**
 * Returns greatest common divisor of the given numbers
 * @param a number 1
 * @param b number 2
 * @return gcd(a, b)
 */


int main(){
	ifstream infile("in.txt");
	long time;
	infile >> time;

	string lines;
	getline(infile, lines);
	getline(infile, lines);

	vector<string> lines_split = split(lines, ',');
	vector<long> l;
	long largest = INT_MIN;
	int position = 0;
	for (int i = 0; i < lines_split.size(); i++){
		string s = lines_split[i];
		if (s.compare("x") == 0)
			l.push_back(-1);
		else{
			long n = stoi(s);
			l.push_back(n);
			if (largest < n){
				largest = n;
				position = i;
			}
		}
	}

	long i = 100000000000000;

	while(true){
		if ((i + position) % largest == 0)
			break;
		i++;
	}
	int increase = 1;
	while (true){
		if (i % 100000000 == 0)
			cout << i << endl;
		for (long j = 0; j < l.size(); j++){
			if (l[j] != -1 && ((i + j) % l[j] != 0))
				goto next;
		}
		break;
		next:
		i += largest;
	}

	// for (int n : l) {
	// 	int s = 0;
	//
	// 	while (s < time){
	// 		s+=n;
	// 	}
	// 	if (wait_time > s - time){
	// 		wait_time = s - time;
	// 		result = wait_time * n;
	// 	}
	//
	// }
	cout << i << endl;
	return 0;
}
