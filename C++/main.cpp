#include <iostream>
#include <vector>

#include "LeetCode.h"

using namespace std;

int main()
{
  LeetCode leet;
  
  // Max product call
  vector<int> nums = {3,4,5,2};
  cout << leet.maxProduct(nums);
  
  // Add spaces call
  string s="LeetcodeHelpsMeLearn";
  vector<int> spaces = {8,13,15};

  cout << leet.addSpaces(s, spaces);
  
  // Minimum time to Fill Cups
  vector<int> amount = {1, 4, 2};
  cout << leet.fillCups(amount);
  
  // First minimum positive integer
  vector<int> nums = {1, 1, 2, 3, 4, 4};
  cout << leet.firstMissingNumber(nums);
  
  return 0;
}
