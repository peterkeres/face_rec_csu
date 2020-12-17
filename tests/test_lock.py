'''
a Test that checks the lock mod
'''

from lock_mod.lock import Lock
import time

print("hello, testing the lock mod");

time.sleep(3)
print('locking the lock')
testlock = Lock(18)

time.sleep(3)
testlock.unlock()
print('unlocking the lock')

time.sleep(3)
print('end')