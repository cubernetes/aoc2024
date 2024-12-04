#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int find_right(const vector<string>& grid, int i, int j) {
	if (j > (int)grid[i].size() - 4)
		return 0;
	string chars(string(1, grid[i][j]) + grid[i][j + 1] + grid[i][j + 2] + grid[i][j + 3]);
	if (chars == "XMAS" || chars == "SAMX")
		return 1;
	return 0;
}

int find_down(const vector<string>& grid, int i, int j) {
	if (i > (int)grid.size() - 4)
		return 0;
	string chars(string(1, grid[i][j]) + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j]);
	if (chars == "XMAS" || chars == "SAMX")
		return 1;
	return 0;
}

int find_down_right(const vector<string>& grid, int i, int j) {
	if ((i > (int)grid.size() - 4) || (j > (int)grid[i].size() - 4))
		return 0;
	string chars(string(1, grid[i][j]) + grid[i + 1][j + 1] + grid[i + 2][j + 2] + grid[i + 3][j + 3]);
	if (chars == "XMAS" || chars == "SAMX")
		return 1;
	return 0;
}

int find_down_left(const vector<string>& grid, int i, int j) {
	if ((i > (int)grid.size() - 4) || (j < 3))
		return 0;
	string chars(string(1, grid[i][j]) + grid[i + 1][j - 1] + grid[i + 2][j - 2] + grid[i + 3][j - 3]);
	if (chars == "XMAS" || chars == "SAMX")
		return 1;
	return 0;
}

int find_xmas(const vector<string>& grid, int i, int j) {
	int subtotal(0);

	subtotal += find_right(grid, i, j);
	subtotal += find_down(grid, i, j);
	subtotal += find_down_right(grid, i, j);
	subtotal += find_down_left(grid, i, j);
	return subtotal;
}

int main() {
	ifstream file("in.txt");
	string line;
	int total(0);
	vector<string> grid;

	while (getline(file, line))
		grid.push_back(line);

	for (int i = 0; i < (int)grid.size(); ++i)
		for (int j = 0; j < (int)grid[i].size(); ++j)
			total += find_xmas(grid, i, j);
	cout << total << '\n';
	return 0;
}
