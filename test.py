from lock import Lock
import time

print("hello");

time.sleep(3)
testlock = Lock(18)

testlock.unlock()
time.sleep(3)

print('end')