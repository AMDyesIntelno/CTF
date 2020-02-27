# 对Misc题的总结与记录 #


### pyc离线反编译 ###

[源地址](https://github.com/rocky/python-uncompyle6/)

`uncompyle6 *.pyc > *.py`

### Shellcodeexec ###

[源地址](https://github.com/inquisb/shellcodeexec)

***例题***

[PCTF 2016(jarvisoj)](https://dn.jarvisoj.com/challengefiles/shellcode.06f28b9c8f53b0e86572dbc9ed3346bc)

***Sample***

![](https://github.com/AMDyesIntelno/CTF/blob/master/Images/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE_%E9%80%89%E6%8B%A9%E5%8C%BA%E5%9F%9F_20200227115918.png)

### 利用cloacked-pixel进行LSB隐写提取 ###

[源地址](https://github.com/livz/cloacked-pixel)

提取：

`python lsb.py extract a.png out keyword(秘钥)`

a.png位于cloacked-pixel文件夹中
