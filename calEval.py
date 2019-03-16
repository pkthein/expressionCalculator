# calEval.py
# Author Phyo Htut

class Operator:

  def __init__(self, c, p):
    self.cmd = c
    self.prior = p

def exe(cmd, o1, o2):
  if cmd == '+':
    return o1 + o2
  elif cmd == '-':
    return o1 - o2
  elif cmd == '*':
    return o1 * o2
  elif cmd == '/':
    return o1 / o2
  elif cmd == '^':
    return o1 ** o2

delim = '+-=*/^()'

prio = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}

def eva(exp):
  opn = []
  opr = []

  token = ''
  pBump = 0
  
  for c in exp:
    
    if c not in delim:
      token += c
    else:
      if c == '(':
        pBump += 3
      elif c == ')':
        pBump -= 3
      else:
        opn.append(int(token.strip()))
        token = ''
        
        if len(opr) == 0:
          opr.append(Operator(c, prio.get(c) + pBump))
        else:
          
          while len(opn) >= 2 and ( opr[len(opr) - 1].prior >= prio.get(c) + pBump):
            op2 = opn.pop()
            op1 = opn.pop()
            cd = opr.pop().cmd

            opn.append(exe(cd, op1, op2))
          opr.append(Operator(c, prio.get(c) + pBump))


  opn.append(int(token.strip()))

  while len(opn) >= 2:
    op2 = opn.pop()
    op1 = opn.pop()
    cd = opr.pop().cmd

    opn.append(exe(cd, op1, op2))

  return opn[0]
  