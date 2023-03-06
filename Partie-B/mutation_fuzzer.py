import random

import url_parser
from fuzzingbook.MutationFuzzer import MutationFuzzer

RANDOM_SEED = 2230468
random.seed(RANDOM_SEED)
seed = "https://www.polymtl.ca/"
mutation_fuzzer = MutationFuzzer([seed])

valid_inputs = set()
trials = 40

for i in range(trials):
    inp = mutation_fuzzer.fuzz()
    print("input " + inp)
    if url_parser.is_valid_url(inp):
        valid_inputs.add(inp)
print(f"The random seed is: {RANDOM_SEED}")

percentage_of_valid_url = (len(valid_inputs) / trials)*100


print("%s of the generated inputs are valid URLs" % percentage_of_valid_url)
