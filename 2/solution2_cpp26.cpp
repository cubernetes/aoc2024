#include <algorithm>
#include <ranges>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <print>

using namespace std;

// WARNING: This is actually C++26, since it's using ranges::concat_view
// SEE: https://en.cppreference.com/w/cpp/ranges/concat_view
// REQUIRES: g++-15 (not released yet, build from source)
// Compile and run in godbolt: https://godbolt.org/z/49KGcr33j

int main() {
	ifstream file("in.txt");
	string line;
	int n_safe{};

	while (getline(file, line)) {
		if (line.empty())
			continue;
		stringstream ss(line);
		vector<int> nums = views::istream<int>(ss) | ranges::to<vector>();
		bool safe;

		for (int i = -1; i < static_cast<int>(ranges::size(nums)); ++i) {
			// n+1 iterations: one with no element removed, and n iterations with each element removed
			vector<int> nums_copy = i != -1 ? views::concat(nums | views::take(i), nums | views::drop(i + 1)) | ranges::to<vector>() : nums;

			int increasing = ranges::all_of(views::zip(nums_copy, nums_copy | views::drop(1)), [](const auto& zipped){return get<1>(zipped) - get<0>(zipped) > 0;});

			// every difference must be 1, 2, or 3. if not increasing, multiply by -1. i know this is a second pass through the vector, so less efficient, but it's much less error prone than setting flags manually
			if (ranges::all_of(views::zip(nums_copy, nums_copy | views::drop(1)), [&increasing](const auto& zipped){int d = (get<1>(zipped) - get<0>(zipped)) * (2 * increasing - 1); return d == clamp(d, 1, 3);})) {
				n_safe += 1;
				break;
			}
		}
	}
	println("{}", n_safe);
	return 0;
}
