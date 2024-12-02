#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

int main() {
	std::ifstream is("in.txt");
	std::string line;
	int n_safes(0);

	while (getline(is, line))
	{
		if (line.empty())
			continue;
		std::stringstream ss(line);
		std::vector<int> nums;
		int n;

		while (ss >> n) {
			nums.push_back(n);
		}

		std::vector<int>::iterator it = nums.begin();
		int i(0);
		bool outer_first = true;
		bool safe = true;
		while (it != nums.end()) {
			int prev = -1;
			std::vector<int> diffs;
			std::vector<int> nums_copy = nums;

			if (!outer_first) {
				nums_copy.erase(nums_copy.begin() + i);
			}

			for (std::vector<int>::iterator it = nums_copy.begin(); it != nums_copy.end(); ++it) {
				if (prev != -1) {
					diffs.push_back(*it - prev);
				}
				prev = *it;
			}

			bool increasing;
			bool first = true;
			safe = true;
			for (std::vector<int>::iterator it = diffs.begin(); it != diffs.end(); ++it) {
				if (first)
					increasing = *it > 0;
				first = false;
				if (increasing) {
					if (*it < 1 || *it > 3) {
						safe = false;
						break;
					}
				} else {
					if (*it > -1 || *it < -3) {
						safe = false;
						break;
					}
				}
			}
			if (safe)
				break;
			if (!outer_first) {
				++i;
				++it;
			}
			outer_first = false;
		}
		if (safe)
			n_safes += 1;
	}
	std::cout << n_safes << '\n';
	return 0;
}
