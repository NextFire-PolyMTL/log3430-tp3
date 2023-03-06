from fuzzingbook.Fuzzer import RandomFuzzer
import traceback # to get the stack trace
import random
import test_script
random.seed(2020) # to fix the randomness



random_fuzzer = RandomFuzzer()
trials = 100
for i in range(0, trials):
    inp = random_fuzzer.fuzz()
    print ("trial: %s \ninput: %s" % (i, inp))
    try: 
        test_script.crash_if_too_long(inp)
    except ValueError:
        traceback.print_exc()
        break