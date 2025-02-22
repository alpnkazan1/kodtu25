import time
from memory_profiler import profile

    
@profile
def q6():
  a, c = map(int, input().split())

  for b in range(a, 10001):
    s = ""
    for i in range(a, b + 1):
      s += str(i)

    try:
      num = int(s)
      if num % c == 0:
        print(b)
        return
    except ValueError:
      print(-1)
      return

start_time = time.time()
q6()
end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.4f} seconds")