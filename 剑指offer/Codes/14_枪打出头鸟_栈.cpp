using namespace std;

#include<iostream>
#include<vector>

class Solution {
public:
    /**
     * 
     * @param n int整型 n个人
     * @param a int整型vector ai代表第i个人的高度
     * @return long长整型
     */
    long long solve(int n, vector<int>& a) {
        int i = n-1;
        long long SUM = 0;
        while (i > 0){
            for (int j = i-1; j >= 0; j--){
                if (a[j] > a[i]){
                    SUM += j+1;
                    break;
                }
            }
            i --;
        }
        return SUM;
    }
};


int main(){
    int n = 5;
    Solution s = Solution();
    // int a[5] = {1, 2, 3, 4, 5};
    int a[5] = {5, 4, 3, 2, 1};
    vector<int> obj;
    for(int i=0; i < n; i++){
        obj.push_back(a[i]);
    }
    cout << s.solve(n, obj) << endl;
}