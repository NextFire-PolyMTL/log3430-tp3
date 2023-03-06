from fuzzingbook.MutationFuzzer import MutationFuzzer
import random
import url_parser

random.seed(2020)
seed = "https://www.google.com"
mutation_fuzzer = MutationFuzzer([seed])

valid_inputs = set()
trials = 20

for i in range(trials):
    inp = mutation_fuzzer.fuzz()
    print ("input " + inp)
    if url_parser.is_valid_url(inp):
        valid_inputs.add(inp) 

percentage_of_valid_url = (len(valid_inputs)/ trials)*100
        
        
print ("%s of the generated inputs are valid URLs" % percentage_of_valid_url)