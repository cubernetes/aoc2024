#include <cstdio>
#include <fstream>
#include <vector>
#include <print>
#include <map>
#include <algorithm>
#include <set>
#include <ranges>

auto approach1() -> int {
	std::ifstream file("in.txt");

	if (!file) {
		std::println(stderr, "Failed to open file.");
		return 1;
	}

	namespace ranges = std::ranges;
	namespace views = std::views;

	std::vector<int> left;
	std::map<int, int> counts;
	ranges::for_each(views::istream<int>(file) | views::chunk(2), [&left, &counts](const auto& chunk){
		auto it = chunk.begin();
		left.emplace_back(*it);
		++it;
		++counts[*it];
	});
	int sum = ranges::fold_left(
		left | views::transform([&counts](const auto& l){ return l * counts[l]; }),
		0,
		std::plus<int>()
	);

	std::println("{}", sum);

	return 0;
}

int main() {
	return approach1();
}
