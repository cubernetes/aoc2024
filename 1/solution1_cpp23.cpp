// run on godbolt: https://godbolt.org/z/7hM3bno3x

#include <algorithm>
#include <fstream>
#include <vector>
#include <sstream>
#include <ranges>
#include <typeinfo>

#include <string_view>
template <typename T>
constexpr auto type_name() {
  std::string_view name, prefix, suffix;
#ifdef __clang__
  name = __PRETTY_FUNCTION__;
  prefix = "auto type_name() [T = ";
  suffix = "]";
#elif defined(__GNUC__)
  name = __PRETTY_FUNCTION__;
  prefix = "constexpr auto type_name() [with T = ";
  suffix = "]";
#elif defined(_MSC_VER)
  name = __FUNCSIG__;
  prefix = "auto __cdecl type_name<";
  suffix = ">(void)";
#endif
  name.remove_prefix(prefix.size());
  name.remove_suffix(suffix.size());
  return name;
}

// for easy printing of vectors
// fmt.dev/latest/get-started
#include <fmt/ranges.h>

using namespace std;

int main() {
	ifstream s("in.txt");

	vector<pair<int, int>> R, L = R = views::istream<int>(s)
		| views::chunk(2)
		| views::transform([](auto&& chunk) -> pair<int, int> {
				auto it = chunk.begin();
				return pair{static_cast<int>(*it), *++it};
			})
		| ranges::to<vector>();

	// fmt::println("{}", L); // when removing the static_cast above, the tuples in L will have the same 2 values, namely the one from the 2nd dereferencing

	ranges::sort(L, less{}, [](auto&& p){ return get<0>(p); });
	ranges::sort(R, less{}, [](auto&& p){ return get<1>(p); });

	int sum = ranges::fold_left(views::zip_transform([](auto&& l, auto&& r){
				return abs(get<0>(l) - get<1>(r));
			}, L, R),
		0, plus{});

	fmt::println("{}", sum);
	return 0;
}
