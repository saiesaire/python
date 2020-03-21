# coding:utf-8

def sample(x):
  if (x % 3 == 0):
    print(x,"は3の倍数です")
  elif (x % 2 == 0):
    print(x,"は偶数です")
  else:
    print(x,"はそれ以外の数")

print("""５です
５なんです
４じゃありません""")
x = 5
for x in range(1, 20 + 1):
  y = sample(x)
