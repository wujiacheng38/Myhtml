

#任意进制转化成十进制
int_to_char = '0123456789ABCDEF'
char_to_int = {}
for idx,char in enumerate(int_to_char):
    char_to_int[char] = idx
# print(char_to_int)
def k_to_ten(k,x): #k进制数字x转换成10进制数
    ans = 0
    x = x[::-1]
    for i in range(len(x)):
        ans = ans + char_to_int[x[i]] * k ** i
    return ans
k = int(input())
x = input()
print(k_to_ten(k,x))

