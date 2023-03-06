import random

import matplotlib.pyplot as plt
from fuzzingbook.Coverage import Coverage
from fuzzingbook.Fuzzer import Fuzzer, RandomFuzzer
from fuzzingbook.MutationFuzzer import MutationFuzzer
from num2words import num2words

# Règle la graine aléatoire
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

# Ajout du paramètre label afin de pouvoir les différencier dans le graphique
def plot(cumulative_coverage, label: str):
    plt.plot(cumulative_coverage, label=label)
    plt.title('Coverage')
    plt.xlabel('# of inputs')
    plt.ylabel('lines covered')


class MyFuzzer(Fuzzer):

    def fuzz(self) -> str:
        # Renvoie la chaîne de caractères d'un nombre aléatoire
        # compris entre -1e100 et 1e100
        return str(random.randint(-1e100, 1e100))


# Nombre d'itérations
trials = 500

# Fuzzers testés
fuzzers = dict(
    random=RandomFuzzer(),
    mutation=MutationFuzzer(seed=["3452020"]),
    my_fuzzer=MyFuzzer(),
)

# Itération sur les fuzzers
for name, fuzzer in fuzzers.items():
    # Génération des entrées
    input_set = []
    for i in range(0, trials):
        input_set.append(fuzzer.fuzz())
    # Calcul de la couverture
    cumulative_coverage = calculate_cumulative_coverage(input_set, num2words)
    # Ajout de la courbe dans le graphique
    plot(cumulative_coverage, label=name)

# Affichage du graphique avec les légendes
plt.legend()
plt.show()
