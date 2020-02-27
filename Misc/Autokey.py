# -*- coding: utf-8 -*

from pycipher import Autokey
#注意调整大小写及补充数字
print Autokey('AutomaticKey').decipher('fftu{2028mb39927wn1f96o6e12z03j58002p}')
#AutomaticKey为key的内容     fftu{2028mb39927wn1f96o6e12z03j58002p}为要解密的内容
#输出结果为 FLAGABDFDEABEE
#最终结果应为 flag{2028ab39927df1d96e6a12b03e58002e}