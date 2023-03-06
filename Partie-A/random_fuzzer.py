import random
import traceback  # to get the stack trace

import test_script
from fuzzingbook.Fuzzer import RandomFuzzer

SEED = 2089776
random.seed(SEED)  # to fix the randomness


random_fuzzer = RandomFuzzer()
trials = 100
for i in range(0, trials):
    inp = random_fuzzer.fuzz()
    print("trial: %s \ninput: %s" % (i, inp))
    print(f"The random seed is: {SEED}")
    try:
        test_script.crash_if_too_long(inp)
    except ValueError:
        traceback.print_exc()
        break
