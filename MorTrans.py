import sys
argc = sys.argv.__len__()
a2mo_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
             'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
             'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
             'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
             'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
             '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
             '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
             }
mo2a_dict = dict(zip(a2mo_dict.values(), a2mo_dict.keys()))
def mo2a(a):
    '''
    将摩斯密码转换为英文字母或数字
    '''
    det=""
    for i in a:
        det+=mo2a_dict.get(i)
    return det
def a2mo(a):
    '''
    将英文字母或数字转换为摩斯密码
    '''
    det=""
    for i in a:
        det+=a2mo_dict.get(i)
        det+=" "
    return det

if(argc<2):
    print("本脚本为摩斯电码翻译脚本,请输入py MorTrans.py -h以获得使用帮助")
    exit()
if(argc==2):
    if(sys.argv[1]!="-h"):
        print("参数错误,请输入py MorTrans.py -h以获得使用帮助")
    else:
        print("本脚本提供以下命令: ")
        print("py MorTrans.py [-j] [Src], 将字符串Src由摩斯电码翻译为英文字母或数字")
        print("py MorTrans.py [-b] [Src], 将字符串Src由英文字母或数字翻译为摩斯电码")
        print("py MorTrans.py [-h], 显示帮助文本")
    exit()
if(argc==3):
    text=sys.argv[2]
    if(sys.argv[1]=="-j"):
        print(mo2a(text.strip().split(" ")))
    elif(sys.argv[1]=="-b"):
        print(a2mo(text))
    else:
        print("参数错误,请输入py MorTrans.py -h以获得使用帮助")
    exit()