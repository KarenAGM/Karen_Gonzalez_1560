#algoritmo no recursivo
"""
def fibonachi(n):
      primero=0
      segundo=1
      siguiente=0
      for c in range(1,n+1,1):
          if c < 1:
            siguiente=c
            else:
                  siguiente=primero+segundo
                  primero=segundo
                  segundo=siguiente
            return siguiente

print(fibonachi(5))      
 """
def fib_rec(n):
      if n==1 or n==0:
            return 1
      else:
            return fib_rec(n-1)+fib_rec(n-2)

print(fib_rec(5))      
