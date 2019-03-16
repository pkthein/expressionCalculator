# testCal.py
# Author : Phyo Htut

import calEval

def main():
  print("Running Test 0")
  exp = "3 * 2 ^ 4 - 5"
  print(exp)
  print(calEval.eva(exp))

  print("\nRunning Test 1")
  exp = " 3 + 2"
  print(exp)
  print(calEval.eva(exp))

  print("\nRunning Test 2")
  exp = "((1 + 2) + 4) * 3"
  print(exp)
  print(calEval.eva(exp))
  
  print("\nRunning Test 3")
  exp = '(((3 - 2)^3 - 5) * 3 - 2) + 5 * 2 ^ 3'
  print(exp)
  print(calEval.eva(exp))
