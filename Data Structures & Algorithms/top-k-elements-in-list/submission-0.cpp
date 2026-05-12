#include<bits/stdc++.h>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
        unordered_map<int,int> mpp;
        for(auto x : nums){
            mpp[x]++;
        }
        int n = nums.size();
        while(k>0 && n>=1){
            for(auto x : nums){
                if(mpp[x] == n && find(result.begin(), 
                 result.end(), x) == result.end()){
                    result.emplace_back(x);
                    k--;
                }
            }
            n--;
        }
        return result;
    }
};
