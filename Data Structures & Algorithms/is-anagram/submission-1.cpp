class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> mpp;
        int count=0;
        for(auto x : s){
            mpp[x]++;
            count++;
        }
        for(auto x : t){
            if(mpp[x] == 0){
                return false;
            }
            mpp[x]--;
            count--;
        }
        if(!count){return true;}
        else{
            return false;
        }
    }
};
