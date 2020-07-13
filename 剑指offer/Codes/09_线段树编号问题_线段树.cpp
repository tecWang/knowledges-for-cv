using namespace std;

#include<vector>
#include<iostream>

class Solution {
public:
    vector<int> wwork(int n, int* a, int aLen) {
        vector<int> result(n);
        for(int i = 0; i != n; ++i){
            int high = a[i];
            int mid;
            result[i] = 1;
            while (high > 1){
                mid = high/2;
                if(high % 2 == 1 && ((mid&(mid-1)) == 0)){
                    high = mid + 1;
                    result[i] *= 2;
                }
                else{

                    high = mid;
                    result[i] = result[i]*2 + 1;
                }
            }
        }
        return result;
    }
};

int main(){
    Solution s = Solution();
    int a[2] = {4,5};
    s.wwork(2, a, 2);

}