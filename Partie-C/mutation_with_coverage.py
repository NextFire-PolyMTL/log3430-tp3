import random

import matplotlib.pyplot as plt
from fuzzingbook.Coverage import Coverage
from fuzzingbook.Fuzzer import Fuzzer, RandomFuzzer
from fuzzingbook.MutationFuzzer import MutationFuzzer
from num2words import num2words

RANDOM_SEED = 2089776
random.seed(RANDOM_SEED)


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


def plot(cumulative_coverage, label: str):
    plt.plot(cumulative_coverage, label=label)
    plt.title('Coverage')
    plt.xlabel('# of inputs')
    plt.ylabel('lines covered')


class MyFuzzer(Fuzzer):

    def fuzz(self) -> str:
        return str(random.randint(0, 1e100))


trials = 500

fuzzers = dict(
    random=RandomFuzzer(),
    mutation=MutationFuzzer(seed=["3452020"]),
    my_fuzzer=MyFuzzer(),
)

for name, fuzzer in fuzzers.items():
    input_set = []
    for i in range(0, trials):
        input_set.append(fuzzer.fuzz())
    cumulative_coverage = calculate_cumulative_coverage(input_set, num2words)
    plot(cumulative_coverage, label=name)

plt.legend()
plt.show()
