import random
import matplotlib.pyplot as plt


v = {"kort": 150, "kompas": 35, "vand": 200, "sandwich":160, "sukker":60,"dåsemad": 45,"banan":60, "æble":40, "ost": 30, "øl": 10, "solcreme":70, "kamera":30, "T-shirt":15, "bukser":10, "paraply": 40, "vandtætte bukser": 70, "vandtæt overtøj": 75, "pung": 80, "solbriller": 20, "håndklæde":12, "sokker": 50, "bog":10, "notesbog": 1, "telt": 150}
weights = {"kort": 90, "kompas": 130, "vand": 1530, "sandwich":500, "sukker":150,"dåsemad": 680,"banan":270, "æble":390, "ost": 230, "øl": 520, "solcreme":110, "kamera":320, "T-shirt":240, "bukser":480, "paraply": 730, "vandtætte bukser": 420, "vandtæt overtøj": 430, "pung": 220, "solbriller": 70, "håndklæde":180, "sokker": 40, "bog":300, "notesbog": 900, "telt": 2000}
values = list(v.values())
weights = list(weights.values())
items = list(v.keys())
geneLength = len(v)
mutationChance = 0.005

class Gene:
    def __init__(self, gene_length, max_weight):
        self.genes = []
        self.backpack = []
        self.max_weight = max_weight
        for _ in range(gene_length):
            self.genes += [random.randint(0,1)]

    def __eq__(self, other):
        return self.genes == other.genes
        
    def backPack(self):
        self.backpack = []
        [self.backpack.append(items[x]) for x in range(geneLength) if self.genes[x] == 1]
        return self.backpack

    def fitness(self):
        index = 0
        fitness_score = 0
        weight = 0
        for i in self.genes:
            fitness_score += values[index]*i
            weight += weights[index]*i
            index += 1
            if weight > self.max_weight:
                return fitness_score**2*0.2 #Bliver tasken overfyldt, vægtes genet markant mindre
        return fitness_score**3

    def value(self):
        self.score = 0
        index = 0
        weight = 0
        for i in self.genes:
            self.score += values[index]*i
            weight += weights[index]*i
            index += 1
            if weight > self.max_weight:
                return 0
        return self.score

    def mutate(self):
        for i in range(len(self.genes)):
            if random.random() <= mutationChance:
                self.genes[i] = 1-self.genes[i]
        self.backPack()


class main:
    def __init__(self):
        self.populationSize = int(input("Input population size: "))
        self.generations = int(input("Input number of generations: "))
        self.population = [] #Populationen af gener
        self.number_solutions = [] #Liste af gener som giver den højeste værdi (for denne opgave findes kun en løsning som giver 1130, men ændres der på opgaven ville flere løsninger komme i listen)
        self.maxFitScore = 0 #Variabel for den højeste fitness-score eller i andre ord værdi fundet
        self.max_fitness = [] #Liste som indeholder den højeste fitness score for hver generation
        self.av_fitness = [] #Liste som indeholder gennemsnitlige fitness score for hver generation
        self.min_fitness = [] #Liste som indeholder mindste fitness score for hver generation

        for i in range(self.populationSize):
            self.population.append(Gene(len(values), 5000))

    def mate(self):
        #Her muterer generne måske (1% chance for hvert "gen-tal"
        [i.mutate() for i in self.population]
        #Fitness-scoren regnes ud for alle individer i populationen
        fitness_population = [i.fitness() for i in self.population] 
        newGen = [] 
        for i in range(len(self.population)):
            #To parents vælges tilfældigt (Deres fitness score bliver vægtet)
            parents = random.choices(self.population, fitness_population, k=2)
            parent_fitness = [i.fitness() for i in parents]
            childrenGenes = []
            for i in range(geneLength):
                #For at lave child, køres genlængden igennem, hvor der trækkes om hvor gen-tallet skal komme fra. Her er fitness scoren igen vægtet    
                child = random.choices(parents, parent_fitness, k=1)
                #"Gen-Tallet" trækkes ud fra den valgte parent og lægges i listen af child genet
                childrenGenes.append(child[0].genes[i])
            childGene = Gene(geneLength, 5000)
            childGene.genes = childrenGenes
            #Genet tilføjes til den nye generation
            newGen.append(childGene)
        #Populationen bliver erstattet af den nye generation
        self.population = newGen
        
    
    def maxFit(self): #Finder 
        self.maxFitn = []
        sum_fit = 0 #Summen af hver generations totale fitness score, dette bruges til at regne gennemsnit
        min_fit = [] #Jeg har valgt at listen ikke skal indeholde 0, dvs at jeg finder den mindste værdi som opfylder vægt-kravet. Hvis vægt kravet ikke opfyldes bliver scoren nemlig 0 
        for Gene in self.population:
            self.maxFitn.append(Gene.value())
            sum_fit += Gene.value()
            if Gene.value() >= self.maxFitScore:
                self.maxFitScore = Gene.value()
            if Gene.value() != 0:
                min_fit.append(Gene.value())
        self.max_fitness.append(max(self.maxFitn))
        self.min_fitness.append(min(min_fit))
        self.av_fitness.append(sum_fit/len(self.maxFitn))

        return max(self.maxFitn)

    def num_solutions(self, fit_score): #Alle Gener som har den højeste værdi i hver generation, tilføjes til listen
        [self.number_solutions.append(i) for i in self.population if i.value() == fit_score]
        return self.number_solutions

    def clean_list(self): #Alle løsninger fra forrige generationer, tilføjes til en liste hvis deres value er lig den højeste målte, og at et lignende gen ikke er tilføjet i listen (se __eq__ i gen klassen)
        self.solutions = []
        max_v = max([x.value() for x in self.number_solutions]) 
        [self.solutions.append(x) for x in self.number_solutions if x.value() == max_v and x not in self.solutions]
        return self.solutions

    def run(self):
        maxValue = 0
        solutions = []
        for i in range(int(self.generations)):
            self.mate()
            print("max: ", self.maxFit())
            if (max(self.maxFitn)) >= maxValue:
                maxValue = max(self.maxFitn)
                self.num_solutions(maxValue) #Generne som giver den nye maxValue tilføjes til listen af løsninger
            print("maxValue", maxValue)
            
        solutions = []
        for s in self.clean_list():
            solutions.append((s.backPack(), "Value: " + str(s.value())))
        print("Liste af løsninger: ", solutions)

        plt.plot(self.max_fitness, label = "Max Value")
        plt.plot(self.min_fitness, label = "Min Value")
        plt.plot(self.av_fitness, label = "Average Value")
        plt.legend()
        plt.show()

engine = main()
engine.run()
