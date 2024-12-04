#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct row{
	string instr;
	int num;
	bool visited = false;
};

int main(){
	ifstream infile("in.txt");

	vector<row> data;
	string str;
	while (getline(infile, str)){
		row r;
		r.instr = str.substr(0,3);
		r.num = stoi(str.substr(3, str.length()));
		data.push_back(r);
	}

	int accumulator = 0;
	for (int j = 0; j < data.size(); j++){
		for (int k = 0; k < data.size(); k++)
			data[k].visited = false;

		if(data[j].instr.compare("nop") == 0){
			data[j].instr = "jmp";
		}
		else if(data[j].instr.compare("jmp") == 0){
			data[j].instr = "nop";
		}
		else
			continue;

		int i = 0;
		while (true){
			if (i == data.size())
				goto end;
			if (data[i].visited)
				break;
			data[i].visited = true;
			if (data[i].instr.compare("acc") == 0){
				accumulator += data[i].num;
			}
			else if (data[i].instr.compare("jmp") == 0){
				i += data[i].num;
				continue;
			}
			i++;
		}
		if(data[j].instr.compare("nop") == 0){
			data[j].instr = "jmp";
		}
		else if(data[j].instr.compare("jmp") == 0){
			data[j].instr = "nop";
		}
		accumulator = 0;
	}

	end:
	cout << accumulator << endl;
	return 0;
}
