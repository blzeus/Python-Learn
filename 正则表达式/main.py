# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#\d 代表0-9的任何数字
#\D 除 0 到9的数字以外的任何字符
#\w 任何字母，数字或下划线字符
#\W 除字母，数字和下划线以外的任何字符
#\s 空格，制表符或换行符
#\S 除空格制表符和换行符外的任何字符

import re

#匹配文本中一个或多个数字 + 一个空白字符 + 一个或多个字母/数字/或下划线字符
myRegex = re.compile(r'\d+\s\w+')

out  = myRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(out)

#可以使用方括号自定义一组字符串 如 [aeiouAEIOU]
#也可以使用-来表示数字或字母范围.如[a-zA-Z0-9]匹配所有大小写字母和数字
#在方括号内普通的正则表达式不会被解释如 * ？也不会被转义
#在方括号左括号内加上尖尖符号^就可以取反，表示非方括号内字符

myregex1 = re.compile(r'[aeiouAEIOU]')
myregex2 = re.compile(r'[^aeiouAEIOU]')#匹配非元音字母
out1 = myregex1.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans')
out2 = myregex2.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans')
print(out1)
print(out2)

#插入字符 ^ 和美元字符 $：^必须以某文本开始，$必须以某模式结尾
myregex3 = re.compile(r'Hello$')
out3 = myregex3.findall('Hello world! Hello')
print(out3)
