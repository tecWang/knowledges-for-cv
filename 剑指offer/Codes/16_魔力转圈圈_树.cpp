using namespace std;

#include<vector>
#include<iostream>

class Solution {
public:

    void InOrder(int root, vector<int>& l, vector<int>& r, vector<int>& res){
        if(!root) return;
        root--;
        InOrder(l[root],l,r,res);
        res.push_back(root+1);
        InOrder(r[root],l,r,res);
    }

    void dfs(int root,int cnt,vector<int>& l,vector<int>& r,vector<int>& record){
        if(!root) return;
        root--;
        record[root] = (record[root] + cnt)&1;
        if(record[root]) swap(l[root],r[root]);
        dfs(l[root], record[root], l, r, record);
        dfs(r[root], record[root], l, r, record);
    }

    vector<int> solve(int n, int m, vector<int>& l, vector<int>& r, vector<int>& k) {
        // write code here
        vector<int> record(n);
        for(int i=0;i<m;i++) record[k[i]-1]++;
        cout << "record" << endl;
        for (int i = 0; i < n; i ++){
            cout << record[i] << " ";
        }
        cout << endl;

        dfs(1,0,l,r,record);
        vector<int> res;
        InOrder(1,l,r,res);
        return res;
    }

    vector<int> InOrder2(int root, vector<int>& l, vector<int>& r){
        vector<int> res;
        vector<int> arr_temp;
        while (arr_temp.size() != 0 || root != 0){
            while (root != 0){
                arr_temp.push_back(root);
                root = l[root-1];
            }
            root = arr_temp.back();
            res.push_back(root);
            arr_temp.pop_back();
            if (r[root-1] != 0){
                root = r[root-1];
            }else{
                root = 0;
            }
        }
        return res;
    }

    vector<int> solve2(int n, int m, vector<int>& l, vector<int>& r, vector<int>& k) {
        int node, temp;
        vector<int> arr, data(n);
        for (int i=0; i<m; i++){
            node = k[i];
            arr.push_back(node);
            while (arr.size() != 0){
                node = arr.back();
                arr.pop_back();
                if (l[node-1] != 0) arr.push_back(l[node-1]);
                if (r[node-1] != 0) arr.push_back(r[node-1]);
                if (l[node-1] != 0 || r[node-1] != 0) data[node-1] += 1;
            }
        }
        for (int i = 0; i < data.size(); i++){
            if (data[i] == 0){
                continue;
            }
            if (data[i] % 2 != 0) swap(l[i],r[i]);
        }
        
        // return InOrder(1, l, r);
        vector<int> res;
        InOrder(1, l, r, res);
        return res;
    }
};


int main(){
    Solution s = Solution();
    int obj1[5] = {4, 3, 0, 0, 0};
    int obj2[5] = {2, 0, 0, 5, 0};
    int obj3[3] = {3, 1, 5};

    // int obj1[11] = {2, 4, 6, 8, 0, 10, 0, 0, 0, 0, 0};
    // int obj2[11] = {3, 5, 7, 9, 0, 0, 11, 0, 0, 0, 0};
    // int obj3[3] = {6, 3, 2};

    vector<int> l, r, k;
    for(int i=0; i < end(obj1)-begin(obj1); i++){
        l.push_back(obj1[i]);
    }
    for(int i=0; i < end(obj2)-begin(obj2); i++){
        r.push_back(obj2[i]);
    }
    for(int i=0; i < end(obj3)-begin(obj3); i++){
        k.push_back(obj3[i]);
    }

    vector<int> res = s.solve2(l.size(), k.size(), l, r, k);
    cout << "res" << endl;
    for (int i=0; i < res.size(); i++){
        cout << res[i] << " ";
    }
    cout << endl;
}