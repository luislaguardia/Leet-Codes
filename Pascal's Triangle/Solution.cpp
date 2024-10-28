#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generate(int numRows) {
        std::vector<std::vector<int>> triangle;

        for (int row_num = 0; row_num < numRows; ++row_num) {
            std::vector<int> row(row_num + 1, 1);

            for (int j = 1; j < row_num; ++j) {
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j];
            }

            triangle.push_back(row);
        }

        return triangle;
    }
};
