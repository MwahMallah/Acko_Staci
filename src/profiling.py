from calculator_logic import *
import sys
import cProfile

def derivation(data):
    a: float = execute("/", sum(data), len(data))
    b: float = execute("/", 1, (execute("-", len(data), 1)))
    c: float = sum([execute("^", (execute("-", x, a)), 2) for x in data])
    return float(execute("^", execute("*", b, c), 0.5))


# start of profiling
profiling = cProfile.Profile()
profiling.enable() 

# main part of program
numbers = sys.stdin.read()
data = numbers.split()

for i in range(len(data)):
    data[i] = float(data[i])
result = derivation(data)

print(result)

# end of profiling and print profiling
profiling.disable()  
profiling.print_stats(sort='calls')  