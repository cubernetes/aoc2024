#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int find_x_mas(const vector<string>& grid, int i, int j) {
	if (i == 0 || i == grid.size() - 1 || j == 0 || j == grid[i].size())
		return 0;

	string backslash(string(1, grid[i - 1][j - 1]) + grid[i][j] + grid[i + 1][j + 1]);
	string slash(string(1, grid[i + 1][j - 1]) + grid[i][j] + grid[i - 1][j + 1]);
	if ((backslash == "MAS" || backslash == "SAM") && (slash == "MAS" || slash == "SAM"))
		return 1;
	return 0;
}

int main() {
	ifstream file("in.txt");
	string line;
	int total(0);
	vector<string> grid;

	while (getline(file, line))
		grid.push_back(line);

	for (int i = 0; i < static_cast<int>(grid.size()); ++i)
		for (int j = 0; j < static_cast<int>(grid[i].size()); ++j)
			total += find_x_mas(grid, i, j);
	cout << total << '\n';
	return 0;
}
