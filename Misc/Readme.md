# 对Misc题的总结与记录 #

### png图片根据crc恢复高和宽 ###

python 2.7

```python
# -*- coding: utf-8 -*-
import binascii
import struct
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#\x49\x48\x44\x52   宽度(4位)   高度(4位)   \x08\x06\x00\x00\x00   crc校验码即crc32key(4位)

crc32key = 0x402E2D95
for i in range(0, 65535):
  l = struct.pack('>i', i)
  data = '\x49\x48\x44\x52\x00\x00\x02\x72'+l+'\x08\x06\x00\x00\x00'

  crc32result = binascii.crc32(data) & 0xffffffff

  if crc32result == crc32key:
    print ''.join(map(lambda c: "%02X" % ord(c), l))
```

### 将RGB值转化为图片 ###

```python
# -*- coding: utf-8 -*
from PIL import Image

x=503 #图片尺寸
y=122

im=Image.new("RGB",(x,y))
file=open('a.txt')

for i in range(0,x):
        for j in range(0,y):
                line=file.readline()
                rgb=line.split(",") #将混杂在文本中的逗号去除
                im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))

im.show()
```

### base64隐写 ###

[代码源地址](http://delimitry.blogspot.com/2014/02/olympic-ctf-2014-find-da-key-writeup.html)
```python
def get_base64_diff_value(s1, s2):
 base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
 res = 0
 for i in xrange(len(s1)):
  if s1[i] != s2[i]:
   return abs(base64chars.index(s1[i]) - base64chars.index(s2[i]))
 return res

def solve_stego():
 with open('stego.txt', 'rb') as f:
  file_lines = f.readlines()

 bin_str = ''
 for line in file_lines:
  steg_line = line.replace('\n', '')
  norm_line = line.replace('\n', '').decode('base64').encode('base64').replace('\n', '')

  diff = get_base64_diff_value(steg_line, norm_line)
  pads_num = steg_line.count('=')
  if diff:
   bin_str += bin(diff)[2:].zfill(pads_num * 2)
  else:
   bin_str += '0' * pads_num * 2

 res_str = ''
 for i in xrange(0, len(bin_str), 8):
  res_str += chr(int(bin_str[i:i+8], 2))
 print res_str

solve_stego()
```

***样例***

```
b2Q5dU==
aDk5Ni==
ZG8wOW==
ZzYxYh==
ZjU4NT==
aXBjNF==
Q3dTM2==
d1Y5c1==
dFA3WV==
ZDNQUP==
ejhBMT==
dUowaW==
OVQ2ZD==
aUM5ZU==
NnFFek==
ZGc0T/==
NGpWNE==
NVZpUW==
ejZDTm==
a1VEN5==
azNMUX==
TXlhNW==
bjZwWm==
Q2Q0b1==
```

***输出***
`Ba5e_64OFive`

### pyc离线反编译 ###

[源地址](https://github.com/rocky/python-uncompyle6/)

`uncompyle6 *.pyc > *.py`
