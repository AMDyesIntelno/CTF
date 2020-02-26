[原文地址](https://www.xctf.org.cn/library/details/8723e039db0164e2f7345a12d2edd2a5e800adf7/)

[具体参考](https://wenku.baidu.com/view/6e84cad459eef8c75ebfb3b5.html)

```python
# -*- coding: utf-8 -*

def getKeywordList(keyword):
    normalList = ''
    for i in range(26):
        normalList = normalList + chr(ord('a') + i)
    toCombine = keyword + normalList
    combineList = ''
    for i in toCombine:
        if i in combineList:
            pass
        else:
            combineList = combineList + i
    if len(combineList) == 26:
        return combineList
    else:
        return ''


def replaceChar(keywordList, inputChar):
    if inputChar.isupper():
        return replaceChar(keywordList, inputChar.lower()).upper()
    else:
        return keywordList[ord(inputChar) - 97]


def dereplaceChar(keywordList, inputChar):
    if inputChar.isupper():
        return dereplaceChar(keywordList, inputChar.lower()).upper()
    else:
        return chr(keywordList.find(inputChar) + 97)


def KeywordReplace(toReplace, keyword):
	#keyword 字符替换法 替换函数
    afterReplace = ''
    for i in toReplace:
        if i.isalpha():
            afterReplace = afterReplace + \
                replaceChar(getKeywordList(keyword), i)
        else:
            afterReplace = afterReplace + i
    return afterReplace


def deKeywordReplace(toReplace, keyword):
	#keyword 字符替换法  反替换函数
    afterReplace = ''
    for i in toReplace:
        if i.isalpha():
            afterReplace = afterReplace + \
                dereplaceChar(getKeywordList(keyword), i)
        else:
            afterReplace = afterReplace + i
    return afterReplace

print KeywordReplace('QCTF{cCgeLdnrIBCX9G1g13KFfeLNsnMRdOwf}', 'lovekfc')
print deKeywordReplace('PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}', 'lovekfc')
```
