#encoding=utf-8

##首先将字符串转换为byte类型，然后将byte转换位hex（16进制），最后转换为10进制整数
def str2int(string):
    str_byte = bytes(string, encoding='utf-8')
    #python3.5以后也可使用下面一句话
    #str_byte = string.encode('utf-8')
    str_hex = str_byte.hex()
    str2int = int(str_hex,16)
    return str2int

##上述转换的逆运算，将整数转换为字符串
def int2str(interger):
    int2hex = hex(interger)
    hex2byte = bytes.fromhex(int2hex[2:])
    byte2str = hex2byte.decode('utf-8')
    return byte2str

##加密字符串，成为一个整数密文
def encryption(string, key):
    string2int = str2int(string)
    key2int = str2int(key)
    '''求字符串转整数后的位数，以便对密码转整数后通过倍数计算得到差不多
    相同的位数进行位运算（否则由于位运算的特性用相近的密码也能进行文本大
    部分还原），同时将这个位数储存在密文中，以便解密时使用相同的数字。'''
    len_str = len(str(string2int))
    len_len_str = len(str(len_str))
    len_key = len(str(key2int))
    key_multy = (len_str - len_key) if len_str >len_key else 0
    key_use = key2int * (10**(key_multy+1))
    encry_int = string2int ^ key_use
    return str(len_len_str)+str(len_str)+str(encry_int)

##解密整数密文，根据异或与运算得到ASCII序号。然后翻译
def decryption(string, key):
    key2int = str2int(key)
    '''
    原字符串转化为整数的位数，以及位数的位数已经写到密文中前面部分了
    （之所以要记录两次信息，因为位数是不定长的，可能1个数字可能2、3个
    或更多）
    '''
    len_len_str = int(string[0])
    len_str = int(string[1:len_len_str+1])
    len_key = len(str(key2int))
    key_multy = (len_str - len_key) if len_str >len_key else 0
    key_use = key2int * (10**(key_multy+1))
    translate_string = string[len_len_str+1:]
    decry_int = int(translate_string) ^ key_use
    decry_str = int2str(decry_int)
    return decry_str

def main():
    enter_str = input('请选择 1：加密；2：解密 \n')
    if enter_str == '1':
        while True:
            string = input('请输入加密文本：\n') 
            if len(string) <= 10000:
                break
            else:
                print('字符数太多（加密文本字符数应小于10000）')
        while True:
            key = input('请输入密匙：（密匙不能为空）\n')
            if key != '':
                break
            else:
                pass
        print('密文为：\n'+ encryption(string, key))

    elif enter_str == '2':
        string = input('请输入密文：\n')
        while True:
            key = input('请输入密匙：（密匙不能为空）\n')
            if key != '':
                break
            else:
                pass
        try:
            print('解密为：\n'+ decryption(string, key))
        except Exception as e:
            print('密匙或密文错误！\n')
    else:
        print('选择错误！')
    input('按任意键退出。')
if __name__ == '__main__':
    main()
