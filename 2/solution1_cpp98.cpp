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
		std::vector<int> diffs;
		int prev, n;

		prev = -1;
		while (ss >> n) {
			if (prev != -1) {
				diffs.push_back(n - prev);
			}
			prev = n;
		}
		bool safe = true;
		bool increasing;
		bool first = true;
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
			n_safes += 1;
	}
	std::cout << n_safes << '\n';
	return 0;
}
