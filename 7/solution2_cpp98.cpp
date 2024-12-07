#include <cassert>
#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

bool has_solution(const long& expected, const vector<long>& ints, int idx, char op, long init) {
	if (idx >= ints.size())
		assert(false);

	long intermediate;
	ostringstream s_left;
	ostringstream s_right;
	s_left << init;
	s_right << ints[idx];
	string left(s_left.str());
	string right(s_right.str());
		
	switch (op) {
		case '+':
			intermediate = ints[idx] + init; break;
		case '*':
			intermediate = ints[idx] * init; break;
		case '|':
			intermediate = atol((left + right).c_str()); break;
		default:
			assert(false);
	}

	if (idx == ints.size() - 1)
		return intermediate == expected;

	return has_solution(expected, ints, idx + 1, '+', intermediate) ||
			has_solution(expected, ints, idx + 1, '*', intermediate) ||
			has_solution(expected, ints, idx + 1, '|', intermediate);
}

int main() {
	ifstream file("in.txt");
	string line;
	long total(0);

	while (getline(file, line)) {
		size_t pos = line.find(": ");
		long res = atol(line.c_str());
		stringstream ints_stream(line.substr(pos + 2));
		long num;
		vector<long> ints;
		while (ints_stream >> num) {
			ints.push_back(num);
		}
		if (has_solution(res, ints, 0, '+', 0))
			total += res;
	}
	cout << total << '\n';
	return 0;
}
