# coding:utf-8
import sys

def sample(x):
  if (x % 3 == 0):
    print(x,"は3の倍数です")
  elif (x % 2 == 0):
    print(x,"は偶数です")
  else:
    print(x,"はそれ以外の数")

print("いくつまで表示しますか？")
y = int(input())
print(y,"回")
for x in range(1, y + 1):
  sample(x)
