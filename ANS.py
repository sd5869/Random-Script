import math
"""
The run function in which our solution must be present.
Instead of taking input we need to do ip.readline()
Instead of output we need to do op.write()
"""
def run(ip,op):
    t=ip.readline()
    for _ in range(int(t)):
        x=int(ip.readline())
        op.write(str(int(math.sqrt(x)))+"\n")
