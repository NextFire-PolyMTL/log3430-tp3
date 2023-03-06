from fuzzingbook.MutationFuzzer import MutationFuzzer
from fuzzingbook.Coverage import Coverage
import random
import url_parser
import matplotlib.pyplot as plt

random.seed(2020)

def calculate_cumulative_coverage(input_population, function):
    cumulative_coverage = []
    all_coverage = set()
    
    for inp in input_population:
        with Coverage() as cov:
            try:
                function(inp)
            except:
                # we ignore exceptions for the purpose of this code, but some exceptions may be interesting
                pass
        # set union
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))
    return cumulative_coverage


def plot(cumulative_coverage):
    plt.plot(cumulative_coverage)
    plt.title('Coverage')
    plt.xlabel('# of inputs')
    plt.ylabel('lines covered')


trials = 10
fuzzer = MutationFuzzer(seed = ["http://www.google.com"])
input_set = []
for i in range(0, trials):
    input_set.append(fuzzer.fuzz())
cumulative_coverage = calculate_cumulative_coverage(input_set, url_parser.is_valid_url)
plot(cumulative_coverage)
plt.show()
