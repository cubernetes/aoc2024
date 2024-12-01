// multiple approaches, much help of chatgpt, many c++23 features

#include <cstdio>
#include <fstream>
#include <vector>
#include <print>
#include <algorithm>
#include <set>
#include <ranges>

auto approach1() -> int {
	std::ifstream file("in.txt");

	if (!file) {
		std::println(stderr, "Failed to open file.");
		return 1;
	}

	/* // reaaaally neat, but not what we need
		std::vector<std::pair<int, int>> data;
		int a, b;

		while (file >> a >> b)
			data.emplace_back(a, b); // no copy, no move, call constructor in-place
		
		// for (std::vector<std::pair<int, int>>::iterator i = data.begin();
		// 	i != data.end(); ++i) {
		// 	std::cout << i->first << ';' << i->second << '\n';
		// }

		for (const auto& [i, j] : data) { // structured bindings
			std::cout << i << ';' << j << '\n';
		}
	*/

	namespace ranges = std::ranges;
	namespace views = std::views;

	std::vector<int> vec1, vec2;

	ranges::for_each(views::istream<int>(file) | views::chunk(2),
		[&vec1, &vec2](const auto& chunk){
			auto it = ranges::begin(chunk);
			vec1.emplace_back(*it); it++;
			vec2.emplace_back(*it);
		}
	);

	int sum = ranges::fold_left(
		ranges::zip_view(
				ranges::to<std::multiset>(vec1), // ranges::sort works as well
				ranges::to<std::multiset>(vec2)
			) | views::transform([](const auto& zipped){
				return std::abs(
					std::get<0>(zipped) - std::get<1>(zipped)
				);
			}),
		0,
		std::plus<int>()
	);

	std::println("{}", sum);

	/// Below doesn't work since we're using input iterators which are read-once...
	/// auto first_elements = ints | views::stride(2);
	/// auto second_elements = ints | views::drop(1) | views::stride(2);

	/// auto vec1 = first_elements | ranges::to<std::vector>();
	/// auto vec2 = second_elements | ranges::to<std::vector>();

	/// for (auto v1 : vec1)
	/// 	std::cout << v1 << '\n';

	/// std::cout << '\n';

	/// for (auto v2 : vec2)
	/// 	std::cout << v2 << '\n';

	/// return 0;

	/// // ranges::sort(vec1);
	/// // ranges::sort(vec2);

	/// auto zipped = ranges::zip_view(vec1, vec2);
	/// 
	/// std::cout << "Hello\n";
	/// for (const auto& [l, r] : zipped)
	/// 	std::cout << l << ';' << r << '\n';
	/// std::cout << "After\n";

	/// int total = std::transform_reduce(
	/// 	zipped.begin(), zipped.end(),
	/// 	zipped, 0, std::plus{}, [](const auto& pair) {
	/// 		return std::abs(std::get<0>(pair) - std::get<1>(pair));
	/// 	}
	/// );

	// std::cout << total << '\n';

	return 0;
}

int main() {
	return approach1();
}
