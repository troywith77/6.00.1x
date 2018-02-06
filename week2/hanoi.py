def printMove(fr, to):
  print('Move from ' + fr + ' to ' + to)

# Hanoi 用递归的方法，就是每一次把除了最下一个移到空的地方，然后移动最底下那个，然后把其余移到最底下那个上方

def Tower(n, fr, to, spare):
  # 如果只有一个，直接移动
  if n == 1:
    printMove(fr, to)
    return
  # 把最底下以上的移到空的地方
  Tower(n - 1, fr, spare, to)
  # 把最底下那个移到目的地
  Tower(1, fr, to, spare)
  # 把剩下的移到目的地
  Tower(n - 1, spare, to, fr)

Tower(3, 'P1', 'P2', 'P3')