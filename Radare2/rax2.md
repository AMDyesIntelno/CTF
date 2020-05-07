## rax2 是一个格式转换工具,在二进制 八进制 十六进制数字和字符串之间进行转换 ##

```s
rax2 -h
Usage: rax2 [options] [expr ...]
  =[base]                      ;  rax2 =10 0x46 -> output in base 10
  int     ->  hex              ;  rax2 10
  hex     ->  int              ;  rax2 0xa
  -int    ->  hex              ;  rax2 -77
  -hex    ->  int              ;  rax2 0xffffffb3
  int     ->  bin              ;  rax2 b30
  int     ->  ternary          ;  rax2 t42
  bin     ->  int              ;  rax2 1010d
  ternary ->  int              ;  rax2 1010dt
  float   ->  hex              ;  rax2 3.33f
  hex     ->  float            ;  rax2 Fx40551ed8
  oct     ->  hex              ;  rax2 35o
  hex     ->  oct              ;  rax2 Ox12 (O is a letter)
  bin     ->  hex              ;  rax2 1100011b
  hex     ->  bin              ;  rax2 Bx63
  ternary ->  hex              ;  rax2 212t
  hex     ->  ternary          ;  rax2 Tx23
  raw     ->  hex              ;  rax2 -S < /binfile
  hex     ->  raw              ;  rax2 -s 414141
  -l                           ;  append newline to output (for -E/-D/-r/..
  -a      show ascii table     ;  rax2 -a
  -b      bin -> str           ;  rax2 -b 01000101 01110110
  -B      str -> bin           ;  rax2 -B hello
  -d      force integer        ;  rax2 -d 3 -> 3 instead of 0x3
  -e      swap endianness      ;  rax2 -e 0x33
  -D      base64 decode        ;
  -E      base64 encode        ;
  -f      floating point       ;  rax2 -f 6.3+2.1
  -F      stdin slurp code hex ;  rax2 -F < shellcode.[c/py/js]
  -h      help                 ;  rax2 -h
  -i      dump as C byte array ;  rax2 -i < bytes
  -k      keep base            ;  rax2 -k 33+3 -> 36
  -K      randomart            ;  rax2 -K 0x34 1020304050
  -L      bin -> hex(bignum)   ;  rax2 -L 111111111 # 0x1ff
  -n      binary number        ;  rax2 -n 0x1234 # 34120000
  -o      octalstr -> raw      ;  rax2 -o \162 \62 # r2
  -N      binary number        ;  rax2 -N 0x1234 # \x34\x12\x00\x00
  -r      r2 style output      ;  rax2 -r 0x1234
  -s      hexstr -> raw        ;  rax2 -s 43 4a 50
  -S      raw -> hexstr        ;  rax2 -S < /bin/ls > ls.hex
  -t      tstamp -> str        ;  rax2 -t 1234567890
  -x      hash string          ;  rax2 -x linux osx
  -u      units                ;  rax2 -u 389289238 # 317.0M
  -w      signed word          ;  rax2 -w 16 0xffff
  -v      version              ;  rax2 -v
```

```s
rax2 16 -> 0x10
rax2 -16 -> 0xfffffffffffffff0
将十进制转换为16进制

rax2 0xa -> 10
rax2 0xffffffb3 -> 4294967219
将16进制转换为十进制
```

```s
rax2 b8 -> 1000b
将十进制转换为二进制

rax2 10d -> 2
将二进制转换为十进制
```

```s
rax2 t6 -> 20t
将十进制转换为三进制

rax2 10dt -> 3
将三进制转换为十进制
```

```s
rax2 10o -> 0x8
将八进制转换为16进制

rax2 Ox10(大写O) -> 020
将16进制转换为八进制
```

```s
rax2 101b -> 0x5
将二进制转换为16进制

rax2 Bx5 -> 101b
将16进制转换为二进制
```

```s
rax2 -s 4141 -> AA
将16进制转换为ascii

rax2 -S AAA -> 414141
将ascii转换为16进制

asdf(文件):
ABC
CBA

rax2 -S < asdf -> 4142430a4342410a (0a为换行符)
```

```s
rax2 -a -> 打印ascii表
rax2 -l -> 动态输入输出流
```

```s
rax2 -b 01000101 -> E
rax2 -b 01000101 01000101 -> EE
rax2 -b 0100010101000101 -> EE
将二进制转换为ascii

rax2 -B E -> 01000101
rax2 -B asdf -> 01100001011100110110010001100110
将ascii转换为二进制
```

```s
rax2 -d 10 -> 10
rax2 -d 0x10 -> 16
rax2 -d 10o -> 8
rax2 -d 10b ->2
将其他进制转换为十进制
```

```s
rax2 -e 0x00000033 -> 855638016
rax2 -e 51 -> 0x33000000
rax 855638016 -> 0x33000000
rax 0x33000000 -> 51
交换字节序
```

```s
rax2 -E asdf -> YXNkZg==
rax2 -D YXNkZg== -> asdf
base64译码和解码
```

```s
rax2 -n 0x123 -> 23010000
rax2 -N 0x123 -> \x23\x01\x00\x00
大端转小端
```

```s
rax2 -r 0x123

hex     0x123
octal   0443
unit    291
segment 0000:0123
int32   291
string  "#\x01"
binary  0b0000000100100011
float:  0.000000f
double: 0.000000
trits   0t101210
以r2的风格进行输出
```

```s
rax2 -t 0 -> Thu Jan  1 08:00:00 1970
rax2 -t 1 -> Thu Jan  1 08:00:01 1970
rax2 -t 123456789 -> Fri Nov 30 05:33:09 1973
时间计算器
```

```s
rax2 -u 1024 -> 1K
rax2 -u 1048576 -> 1M
大小计算器
```