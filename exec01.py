"""
正则表达式练习

1. 匹配一个.com邮箱格式的邮箱
2. 匹配一个密码 8-12位 数字字母下划线构成
3. 匹配一个数字,包含整数 小数  正数  负数  分数1/2
和百分数 4.6%
4. 匹配一段文字中以大写字母开头的单词,注意文字中可能
含有 iPython 这种,不算大写字母开头, H-base这种算大写
字母开头,  BSD 也是
"""
import re

print(re.findall(r'\w+@\w+\.com','166456@qq.com'))
print(re.findall(r'\w{8,12}','16_6456WW'))
print(re.findall(r'-?\d+\.?/?\d*%?','12 -3 1.2 1/2 %4 4.3%'))
print(re.findall(r'\b[A-Z][-_a-zA-Z]*','iPython H-base BSD Hello asd asdL'))





