#include <iostream>
#include <vector>

#include "LeetCode.h"

using namespace std;

int main()
{
  LeetCode leet;
  
  vector<int> nums = {3,4,5,2};
  cout << leet.maxProduct(nums);
  return 0;
}
