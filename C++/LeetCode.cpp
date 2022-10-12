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
}

int LeetCode::fillCups(vector<int>& amount) {
    int seconds = 0;
    sort(amount.begin(), amount.end(), greater<int>());
    while (amount[0] > 0)
    {
        amount[0] -= 1;
        amount[1] -= 1;
        seconds += 1;
        sort(amount.begin(), amount.end(), greater<int>());
    }
    return seconds;
}


int LeetCode::firstMissingNumber(vector<int>& nums)
{   
    int curr_min_num = 1;

    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());

    for (int i=0; i<nums.size(); i++)
    {
        if (curr_min_num == nums[i])
        {
            curr_min_num += 1;
        }
        else if (nums[0] > 0)
        {
            return curr_min_num;
        }
    }
    return curr_min_num;
}


int LeetCode::arrayPairSum(vector<int>& nums) 
{
    sort(nums.begin(), nums.end());
    int ans = 0;
            
    for (int i=0; i<nums.size(); i+=2)
    {
        ans += min(nums[i], nums[i+1]);
    }
    return ans;
}

