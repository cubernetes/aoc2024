#include <cctype>
#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

// poor-man's state machine
bool parse_mul(char c, string& left_num, string& right_num) {
	static int state(0);

	if (c == 'm') {
		state = 1;
	} else if (c == 'u' && state == 1) {
		state = 2;
	} else if (c == 'l' && state == 2) {
		state = 3;
	} else if (c == '(' && state == 3) {
		state = 4;
	} else if (isdigit(c) && (state == 4 || state == 5)) {
		left_num += c;
		state = 5;
	} else if (c == ',' && state == 5) {
		state = 6;
	} else if (isdigit(c) && (state == 6 || state == 7)) {
		right_num += c;
		state = 7;
	} else if (c == ')' && state == 7) {
		state = 8;
	} else {
		state = 0;
	}

	if (state == 0) {
		left_num = "";
		right_num = "";
	}

	if (state == 8) {
		state = 0;
		return true;
	}
	return false;
}

int main() {
	ifstream file("in.txt");
	char c;
	int sum(0);
	string n1("");
	string n2("");

	int state(0);
	int idx(0);
	while (file.get(c)) {
		if (parse_mul(c, n1, n2)) {
			sum += atoi(n1.c_str()) * atoi(n2.c_str());
			n1 = "";
			n2 = "";
		}
		++idx;
	}
	cout << sum << '\n';

	return 0;
}