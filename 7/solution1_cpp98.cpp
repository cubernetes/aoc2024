#include <cassert>
#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

bool has_solution(
	const int& expected, // 190
	const vector<int>& ints, // [10, 19]
	int idx, // 0
	char op, // '+', '*'
	int init // 0
) {
	int intermediate;

	if (idx >= ints.size())
		assert(false);
		
	switch (op) {
		case '+':
			intermediate = ints[idx] + init; break;
		case '*':
			intermediate = ints[idx] * init; break;
		default:
			assert(false);
	}

	if (idx == ints.size() - 1)
		return intermediate == expected;

	return has_solution(expected, ints, idx + 1, '+', intermediate) ||
			has_solution(expected, ints, idx + 1, '*', intermediate);
}

int main() {
	ifstream file("in.txt");
	string line;
	int total(0);

	while (getline(file, line)) {
		size_t pos = line.find(": ");
		int res = atoi(line.c_str());
		stringstream ints_stream(line.substr(pos + 2));
		int num;
		vector<int> ints;
		while (ints_stream >> num) {
			ints.push_back(num);
		}
		if (has_solution(res, ints, 0, '+', 0))
			total += res;
	}
	cout << total << '\n';
	return 0;
}
