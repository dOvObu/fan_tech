""" Сейчас выводит что-то такое:
для заданной 2 + 2 * 2
['2']
  ['2'] есть в 2
махнём ['e']
['e', '+']
['e', '+', '2']
  ['e', '+', '2'] есть в 2
махнём ['e', '+', 'e']
['e', '+', 'e', '*']
['e', '+', 'e', '*', '2']
  ['e', '+', 'e', '*', '2'] есть в 2
махнём ['e', '+', 'e', '*', 'e']
  ['e', '+', 'e', '*', 'e'] есть в e*e
махнём ['e', '+', 'e']
  ['e', '+', 'e'] есть в e+e
махнём ['e']
"""
S = '2 + 2 * 2'
s = [c for c in S if c != ' '] # rm ' '

expr = [
   '(e)'
,  'e*e', 'e/e'
,  'e+e', 'e-e'
,  '2'
]
power = [
   3
,  2, 2
,  1, 1
,  0
]

def eq_lists(l1, l2):
   if len(l1) != len(l2): return False
   i = 0
   while len(l1) > i:
      if l1[i] != l2[i]: return False
      i = i + 1
   return True


def is_in(l, r):
   n = 0
   for i in r:
      if eq_lists(l, i): return n
      n = n + 1
   return -1


def starts_with(lst, bgn):
   if len(bgn) > len(lst): return False
   i = 0
   while len(bgn) > i:
      if lst[i] != bgn[i]: return False
      i = i + 1
   return True


def is_in_start(l, r):
   n = 0
   for i in r:
      if starts_with(i, l): return n
      n = n + 1
   return -1

print ('для заданной {}'.format(S))

stack = [] # можно не стек символов, а стек узлов AST дерева

j = 0
for c in s:
   j = j+1
   a = ' ' if j >= len(s) else s[j]
   stack.append(c)
   print (stack)
   i = 0
   while len(stack) > i:
      n = is_in(stack[i:], expr)
      if n != -1:
         p = power[n]

         stack2 = stack[i:]
         stack2.append(a)
         k = 0
         p2 = p
         while len(stack2) - 1 > k:
            n2 = is_in_start(stack2[k:],expr)
            if n2 != -1:
               p2 = power[n2]
               break
            k = k+1
         if p2 > p: break # if p2 >= p: break # для правой ассоциативности

         print('  {} есть в {}'.format(stack, expr[n]))
         stack = stack[:i] # можно не просто обрезать и вставлять, а звать callback-и из правил
         stack.append('e')
         print('махнём {}'.format(stack))
         i = 0
         continue
      i = i+1

print ('\nВсё распарсили, изи катка')
