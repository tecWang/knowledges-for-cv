using namespace std;

#include<iostream>

class Solution {
public:
    long long Pokemonfight(long long HP, long long ACK, long long HP2, long long ACK2) {
        // write code here

        if (HP2<=ACK) return -1;
        if (HP<=ACK2) return 1;

        if (HP2<=2*ACK){
            if(HP<=ACK2 && HP2>ACK2){
                return 1;
            }
            else{
                return -1;
            }
        }

        long long hp_interval = (HP2-2*ACK)%ACK == 0? (HP2-2*ACK)/ACK: (HP2-2*ACK)/ACK+1;
        if(ACK == 1){
            hp_interval = HP2 - 1;
        }
        long long ack_count = HP % ACK2 == 0? HP/ACK2: HP/ACK2+1;
        long long m = 0;
        if(ack_count > hp_interval){
            m = ack_count / hp_interval;
        }
        // 如果interval是1得话，不生效
        if(hp_interval == 1){
            return ack_count*2-2;
        }
        // cout << "ack_count:" << ack_count << " hp_interval:" << hp_interval << " m:" << m << endl;

        if(ack_count - m*hp_interval <= hp_interval+1){
            return ack_count + m;
        }else{
            return ack_count + m + 1;
        }
    }
};

int main(){
    Solution s = Solution();
    cout << s.Pokemonfight(20007002001,1,10000000000,1) << endl;
    cout << s.Pokemonfight(20000000001,1,10000000000,10000000000) << endl;
    cout << s.Pokemonfight(6,1,6,1) << endl;
    cout << s.Pokemonfight(8,3,8,1) << endl;
    cout << s.Pokemonfight(10,3,16,1) << endl;
    cout << s.Pokemonfight(1,1,1,1) << endl;
}