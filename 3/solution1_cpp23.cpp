#include <cstdlib>
#include <print>
#include <regex>
#include <fstream>
#include <charconv>

using namespace std;

int main() {
	ifstream file("in.txt");
	string line;
	regex rx("mul\\((\\d{1,3}),(\\d{1,3})\\)");
	int sum(0);

	while (getline(file, line)) {
		auto matches_begin = sregex_iterator(line.begin(), line.end(), rx);
		auto matches_end = sregex_iterator();
		for (sregex_iterator it = matches_begin; it != matches_end; ++it) {
			smatch match = *it;
			string left_num_s = match.str(1);
			string right_num_s = match.str(2);
			int left_num;
			int right_num;
			from_chars(left_num_s.data(), left_num_s.data()+left_num_s.size(), left_num);
			from_chars(right_num_s.data(), right_num_s.data()+right_num_s.size(), right_num);
			sum += left_num * right_num;
		}
	}
	println("{}", sum);
	return 0;
}
