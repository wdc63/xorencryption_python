# xorencryption_python
2018-11-19

webapp由于flexx采用的pyscript不支持string的encode和decode方法，因此采用对每个字符单独用key加密实现，效率较低，但日日常使用还行。

demo演示地址：http://123.206.114.168:12358/encrypt_decrypt/

================================================================================================================================
2018-11-18
A practical  XOR encryption script can encrypt any string or text written in Python. 一个实用的python按位异或对称加密脚本，可以加密任何文本成数字。

该脚本将string类型通过bytes，hex再转换为10进制数字，根据输入string长度得到更长位的key长度，只进行一次位运算，因此算法复杂度较低。使用的按位异或计算对象为：key*(10**(len(string_int)+1))，根据香农的论文，该加密方式具有安全性。

为了保持密文的美观性，采用了整个非列表也无其他符号的纯数字，为了在解密时还原key，string_int的长度的位数和位数的位数被储存在密文的头部，其中位数的位数是第一位。因此该脚本理论上可以加密大约10**9字节文本，大约为1G。但原始脚本中限制输入为1000字符数。如果自信修改储存位数的位数的位数，那么该脚本加密文本无上限。

webapp准备采用flexx实现，但pyscript目前不支持string的encode和decode方法和bytes对象，暂无较好方法将字符串编码为纯数字，因此最终加密密文呈现方式与脚本程序可能不同。
