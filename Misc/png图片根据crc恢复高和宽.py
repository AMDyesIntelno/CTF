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
