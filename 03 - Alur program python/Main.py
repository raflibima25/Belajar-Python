import time

start_time = time.time()

print("hello world")

# ini adalah comment

"""
comment multiline
"""

for i in range(1, 1000):
  a = 10

a = 10 # variable
print(a)
print(time.time() - start_time, "detik")

# kita bisa mengcompile python yang namanya bytecode
# tujuan nya adalah saat di run akan lebih cepet yang bytecode
# cara mengcompile: buka terminal dan tuliskan
# python -m py_compile Main.py