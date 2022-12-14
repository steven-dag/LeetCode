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
  
  vector<int> nums = {1,4,3,2};
  cout << leet.arrayPairSum(nums);
  
  vector<vector<int>> logs = { {0,3}, {2,5}, {0,9}, {1,15}};
  cout << leet.hardestWorker(10, logs);
  
  vector<int> nums = {1,2,2,1,1,3};
  cout << leet.uniqueOccurrences(nums);
  
  Node* root = newNode(3);
  root->left = newNode(9);
  root->right = newNode(20);
  root->right->left = newNode(15);
  root->right->right = newNode(7);
  
  cout << leet.minDepth(root);
  
  return 0;
}
