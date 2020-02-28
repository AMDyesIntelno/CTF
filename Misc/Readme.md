# 对Misc题的总结与记录 #

![mindmap](https://github.com/AMDyesIntelno/CTF/blob/master/Images/mindmap.png)

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

### 一种用于在Python字节码中嵌入Payload的隐写工具 – Stegosaurus ###

[源地址](https://bitbucket.org/jherron/stegosaurus/src)

用法：`python3 Stegosaurus.py -x *.pyc`

[参考链接](https://www.freebuf.com/sectool/129357.html)


### 音频类隐写 ###

1.使用Audacity进行分析，多留意频谱图以及音频的开头和结尾是否存在杂音

2.使用multimon-ng来解码

	例题：bsidessf-ctf-2017 latlong
	得到一个 wav 文件，用 soxi 查看音频文件的格式
	soxi *.wav
	
	将 wav 文件转换成 raw 文件
	sox -t wav *.wav -esigned-integer -b16 -r 22050 -t raw out.raw

	multimon解码
	multimon -t raw -a AFSK1200 a.raw

### dd分割和cat合并 ###
dd的作用是转换和拷贝文件，我们可以利用它来分割文件，相关的选项如下：

if=filename：输入的文件名

of=finename：输出的文件名

bs=bytes：一次读写的字节数，默认是512bytes(做题时通常设置成1)

skip=blocks:拷贝前，跳过的输入文件的前blocks块，块的大小有bs决定(主要由binwalk的分析结果决定)

`dd if=filein of=fileout bs=1 skip=12345`

用cat将两个文件合并

`cat file1 file2 > file3`

### 二维码&条形码&PDF417 ###
[在线扫描](https://online-barcode-reader.inliteresearch.com/)

![](https://github.com/AMDyesIntelno/CTF/blob/master/Images/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE_%E9%80%89%E6%8B%A9%E5%8C%BA%E5%9F%9F_20200227222756.png)

### 数字密码表 ###
安恒11月月赛

![](https://github.com/AMDyesIntelno/CTF/blob/master/Images/%E6%95%B0%E5%AD%97%E5%AF%86%E7%A0%81%E8%A1%A8.png)
