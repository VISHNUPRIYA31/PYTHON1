import pdb;

def double(x):
       pdb.set_trace()
       print(2/0)
       return x * 2
val = 3
print(f"{val} * 2 is {double(val)}")
