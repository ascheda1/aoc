#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <bits/stdc++.h>
#include <regex>

using namespace std;


int main(){
	ifstream infile("in.txt");

	string line;
	vector<string> lines;
	int counter = 0;
	bool valid = true;
	vector<string> fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"};
	while (getline(infile, line)){
		lines.push_back(line);
		stringstream streamstr(line);
		string str;

		while (streamstr >> str){
			string field = str.substr(0, str.find(':'));
			string data = str.substr(str.find(':') + 1, str.length());

			for (int i = 0; i < 7; i++){
				if (valid && fields[i].compare(field) == 0){
					fields[i] = "0";
					switch(i){
					case 0:
						if (stoi(data) < 1920 || stoi(data) > 2002)
							valid = false;
						break;
					case 1:
						if (stoi(data) < 2010 || stoi(data) > 2020)
							valid = false;
						break;
					case 2:
						if (stoi(data) < 2020 || stoi(data) > 2030)
							valid = false;
						break;
					case 3:
						{
							if (data.length() < 3){
								valid = false;
								break;
							}
							string units = data.substr(data.length() - 2, data.length());
							int value = stoi(data.substr(0, data.length() - 2));

							if ((units.compare("cm") == 0)){
								if (value < 150 || value > 193)
									valid = false;
							}
							else if ((units.compare("in") == 0)){
								if (value < 59 || value > 76)
									valid = false;
							}
							else
								valid = false;

						}
						break;
					case 4:
						if (data.length() != 7 || !regex_match(data, regex("#[0-9a-f]+"))) {
							valid = false;
						}
						break;
					case 5:
						if (!(data.compare("amb") == 0) && !(data.compare("blu") == 0) && !(data.compare("brn") == 0) && !(data.compare("gry") == 0)
												 && !(data.compare("grn") == 0) && !(data.compare("hzl") == 0) && !(data.compare("oth") == 0)){
							valid = false;
						}
						break;
					case 6:
						if (data.length() != 9)
							valid = false;

						for (char c : data){
							if (!isdigit(c))
								valid = false;
						}
						break;
					}
				}
			}
		}

		if (line.empty()){
			for (string s : fields){
				if (!(s.compare("0") == 0) && !(s.compare("cid") == 0)){
					goto step;
				}
			}
			if (valid)
				counter++;
			step:
			valid = true;
			fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"};
		}
	}

	cout << counter << endl;
	return 0;
}
