#include <algorithm>
#include <ranges>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <print>

using namespace std;

int main() {
	ifstream file("in.txt");
	string line;
	int n_safe(0);

	while (getline(file, line)) {
		if (line.empty())
			continue;
		stringstream ss(line);
		vector<int> nums = views::istream<int>(ss) | ranges::to<vector>();

		int increasing = ranges::all_of(views::zip(nums, nums | views::drop(1)), [](const auto& zipped){return get<1>(zipped) - get<0>(zipped) > 0;});
		n_safe += ranges::all_of(views::zip(nums, nums | views::drop(1)), [&increasing](const auto& zipped){int d = (get<1>(zipped) - get<0>(zipped)) * (2 * increasing - 1); return d == clamp(d, 1, 3);});
	}
	println("{}", n_safe);
	return 0;
}
