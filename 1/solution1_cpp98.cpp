#include <algorithm>
#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>

int main() {
	std::ifstream is("in.txt");
	std::string line;
	int l, r, sum(0);
	char *end;
	std::vector<int> L, R;

	while (std::getline(is, line)) {
		l = static_cast<int>(std::strtol(line.c_str(), &end, 10));
		r = static_cast<int>(std::strtol(end, NULL, 10));
		L.push_back(l);
		R.push_back(r);
	}

	std::sort(L.begin(), L.end());
	std::sort(R.begin(), R.end());

	for (std::vector<int>::iterator li = L.begin(), ri = R.begin(); li != L.end(); ++li, ++ri) {
		sum += std::abs(*li - *ri);
	}
	std::cout << sum << '\n';

	return 0;
}
