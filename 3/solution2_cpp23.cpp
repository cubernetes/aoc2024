#include <cstdlib>
#include <print>
#include <regex>
#include <fstream>
#include <charconv>

using namespace std;

int main() {
	ifstream file("in.txt");
	string line;
	regex rx("mul\\((\\d+),(\\d+)\\)|don't\\(\\)|do\\(\\)");
	int sum(0);
	bool do_state(true);

	while (getline(file, line)) {
		auto matches_begin = sregex_iterator(line.begin(), line.end(), rx);
		auto matches_end = sregex_iterator();
		for (sregex_iterator it = matches_begin; it != matches_end; ++it) {
			smatch match = *it;
			string whole_str = match.str();
			if (whole_str == "don't()")
				do_state = false;
			else if (whole_str == "do()")
				do_state = true;

			if (whole_str.starts_with("mul("s) && do_state) {
				string left_num_s = match.str(1);
				string right_num_s = match.str(2);
				int left_num;
				int right_num;
				from_chars(left_num_s.data(), left_num_s.data()+left_num_s.size(), left_num);
				from_chars(right_num_s.data(), right_num_s.data()+right_num_s.size(), right_num);
				sum += left_num * right_num;
			}
		}
	}
	println("{}", sum);
	return 0;
}
