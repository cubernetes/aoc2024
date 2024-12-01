#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <map>

int main() {
	std::ifstream is("in.txt");
	std::string line;
	int l, r, sum(0);
	char *end;
	std::vector<int> L;
	std::map<int, int> m;

	while (std::getline(is, line)) {
		l = static_cast<int>(std::strtol(line.c_str(), &end, 10));
		r = static_cast<int>(std::strtol(end, NULL, 10));
		L.push_back(l);
		m[r] += 1;
	}
	for (std::vector<int>::iterator i = L.begin(); i != L.end(); ++i) {
		sum += *i * m[*i];
	}

	std::cout << sum << '\n';
	return 0;
}
