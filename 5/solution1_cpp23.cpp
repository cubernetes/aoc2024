#include <fstream>
#include <ranges>
#include <fmt/ranges.h>
#include <sstream>
#include <vector>

using namespace std::views;
using namespace std;

int main() {
	ifstream file("test.txt");

	ostringstream str;
	str << file.rdbuf();
	auto rules_updates = str.str() | split("\n\n"sv) | ranges::to<vector<string>>();
	auto updates = rules_updates[1] | split("\n"sv) | views::transform(split(","sv)) | ranges::to<vector<vector<string>>>();
	// too complicated
	fmt::println("{}", updates);
	return 0;
}
