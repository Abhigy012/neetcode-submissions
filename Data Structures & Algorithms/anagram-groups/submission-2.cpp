bool isanagram(string &str1 , string &str2){
    unordered_map<char,int> mpp;
    int count=0;
    for(auto x : str1){
        mpp[x]++;
        count++;
    }
    for(auto x : str2){
        if(mpp[x] == 0){
            return false;
        }
        mpp[x]--;
        count--;
    }
    if(!count){
        return true;
    }
    else{
        return false;
    }

}
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<int,int> mpp;
        int n = strs.size();
        vector<vector<string>> result;
        for(int i=0 ; i<n ; i++){
            if(mpp[i] != 0){
                continue;
            }
            vector<string> temp;
            temp.emplace_back(strs[i]);
            mpp[i]++;
            for(int j=i+1;j<n ; j++){
                if(mpp[j] == 0 && isanagram(strs[i],strs[j]) || (strs[i].empty() && strs[j].empty())){
                    temp.emplace_back(strs[j]);
                    mpp[j]++;
                }

            }
            result.emplace_back(temp);
        }
        return result;
    }
};
