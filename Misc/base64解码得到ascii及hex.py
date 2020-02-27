# -*- coding: utf-8 -*

import binascii
import base64
#在info中输入要解码的base64
info=""
print base64.b64decode(info)
print binascii.b2a_hex(base64.b64decode(info))
