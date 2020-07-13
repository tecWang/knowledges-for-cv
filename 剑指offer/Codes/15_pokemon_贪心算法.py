#
# 
# @param HP long长整型 HP
# @param ACK long长整型 ACK
# @param HP2 long长整型 HP2
# @param ACK2 long长整型 ACK2
# @return long长整型
#
class Solution:
    def Pokemonfight(self , HP , ACK , HP2 , ACK2 ):
        # write code here
        # 每回合开始前评估宝可梦是否需要使用满血复活技能
        count = 0
        init_HP2 = HP2
        
        while HP > 0:
            print(HP2 - 2*ACK, HP, HP2)
        
            if HP2 - 2*ACK > 0:
                # 宝可梦可以进行攻击
                HP -= ACK2
                HP2 -= ACK
                count += 1
            else:
                # 宝可梦需要使用复活技能
                if count == 0:
                    # 如果第一回合就发现自己已经需要回血，则每回合开始都需要回血
                    return -1
                elif HP - ACK2 <= 0 and HP2 - ACK > 0:
                    # 如果此时皮卡丘可以被一击致命且宝可梦不会被提前击杀
                    HP -= ACK2
                    count += 1
                else:
                    HP2 = init_HP2
                    count += 1

        return count

print(Solution().Pokemonfight(10, 3, 16, 1))
# print(Solution().Pokemonfight(8,3,8,1))
# print(Solution().Pokemonfight(1,1,1,1))