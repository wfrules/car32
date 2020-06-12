
import sys
from wifi import Wt
from http import Ht
objWt = Wt()
objWt.conn()
print('wifi ok')
objHt = Ht()
objHt.start()
print('htok')



