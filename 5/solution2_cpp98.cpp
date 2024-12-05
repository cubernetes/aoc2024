#include <cstddef>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

void fix_update(vector<string>& update, map<string, vector<string> > rules) {
	bool sorted = false;

	while (!sorted) {
		sorted = true;
		for (map<string, vector<string> >::iterator rule = rules.begin(); rule != rules.end(); ++rule) {
			string left = rule->first;
			vector<string> rights = rule->second;
			ptrdiff_t index_left = distance(update.begin(), find(update.begin(), update.end(), left));
			if (index_left >= update.size())
				continue;
			for (vector<string>::iterator right = rights.begin(); right != rights.end(); ++right) {
				ptrdiff_t index_right = distance(update.begin(), find(update.begin(), update.end(), *right));
				if (index_right >= update.size())
					continue;
				if (index_left >= index_right) {
					string temp = update[index_left];
					update[index_left] = update[index_right];
					update[index_right] = temp;
					sorted = false;
				}
			}
		}
	}
}

int main() {
	ifstream file("in.txt");
	string line;
	map<string, vector<string> > rules;
	vector<vector<string> > updates;

	while (getline(file, line)) {
		stringstream parts(line);
		string left, right;

		if (line.empty())
			break;
		getline(parts, left, '|');
		getline(parts, right, '|');
		rules[left].push_back(right);
	}

	while (getline(file, line)) {
		stringstream parts(line);
		string part;

		updates.push_back(vector<string>());
		while (getline(parts, part, ','))
			updates.back().push_back(part);
	}

	vector<vector<string> > correct_updates;
	for (vector<vector<string> >::iterator update = updates.begin(); update != updates.end(); ++update) {
		bool correct = true;
		for (map<string, vector<string> >::iterator rule = rules.begin(); rule != rules.end(); ++rule) {
			string left = rule->first;
			vector<string> rights = rule->second;
			ptrdiff_t index_left = distance(update->begin(), find(update->begin(), update->end(), left));
			if (index_left >= update->size())
				continue;
			for (vector<string>::iterator right = rights.begin(); right != rights.end(); ++right) {
				ptrdiff_t index_right = distance(update->begin(), find(update->begin(), update->end(), *right));
				if (index_right >= update->size())
					continue;
				if (index_left >= index_right)
					correct = false;
			}
		}
		if (!correct)
			correct_updates.push_back(*update);
	}

	int sum(0);
	for (vector<vector<string> >::iterator update = correct_updates.begin(); update != correct_updates.end(); ++update) {
		fix_update(*update, rules);
		int mid_idx = update->size() / 2;
		sum += atoi((*update)[mid_idx].c_str());
	}
	cout << sum << '\n';
	return 0;
}
