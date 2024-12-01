#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <ranges>
#include <vector>

using namespace std;

// uses features from
// - c++23 (std::views::zip)
// - c++20 (std::ranges)
// - c++17 (structured bindings)
// - c++11 (stoi, auto)
// stolen from
// https://github.com/vss2sn/advent_of_code/blob/master/2024/cpp/day_01a.cpp
// `g++ -std=c++23`

int main() {
	string input = "test.txt";
	ifstream file(input);
	string line;
	vector<int> l1;
	vector<int> l2;

	while(getline(file, line)) {
		size_t space_idx = line.find(' ');
		l1.push_back(stoi(line.substr(0, space_idx)));
		l2.push_back(stoi(line.substr(space_idx + 1, line.size() - space_idx - 1)));
	}
	ranges::sort(l1);
	ranges::sort(l2);
	long long sum = 0;
	for (const auto& [n1, n2] : views::zip(l1, l2)) {
		sum += abs(n1 - n2);
	}
	cout << sum << '\n';
	return 0;
}
