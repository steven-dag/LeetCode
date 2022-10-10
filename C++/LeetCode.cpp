#include "LeetCode.h"

int LeetCode::maxProduct(vector<int>& nums){
    sort(nums.begin(), nums.end(), greater<int>());
    return (nums[0]-1)*(nums[1]-1);
}


string LeetCode::addSpaces(string s, vector<int>& spaces)
{
    string ans;
    int j = 0;

    for (int i=0; i < s.length(); i++)
    {
        if (spaces[j] == i && j < spaces.size())
        {
            ans += ' ';
            j++;
        }
        ans += s[i];
    }
    return ans;
