import chromo_ops

def parse(text_file):
    '''
    Parses Spline Foil data to readable chromosome format
    :param text_file: directory to aim at
    :return: Returns the chromosome format
    '''
    print("Parsing:", text_file) #Debug

    with open(text_file, 'r') as file:
        data = file.read()
    parsed_data = data.split('\n')
    print("Name of spline foil data:",parsed_data[0])
    new_data = []
    for i in range(1, len(parsed_data)):
        new_data.append(parsed_data[i])
    genes = []
    for i in range(len(new_data)):
        lst = []
        for j in new_data[i].split():
            lst.append(float(j))
        genes.append(lst)
    print("Amount Collected:", len(genes))
    return genes

def parse_set(text_file):
    CHROMOSOMES_PER_SET = 1000
    GENES_PER_CHROMOSOME = 60
    if parse_set is not type(str):
        raise TypeError("Please pass the directory as a string.")
    else:
        chromosomes = []
        print("Parsing Set:", text_file)
        with open(text_file, 'r') as file:
            data = file.read()
        parsed_data = data.split('\n')
        for i in range(CHROMOSOMES_PER_SET):
            genes = []
            print("Parsing", parsed_data[i])
            for j in range(GENES_PER_CHROMOSOME):
                genes.append(parsed_data[(i * GENES_PER_CHROMOSOME) + (j+1)])
            print(genes)
            chromosomes.append(genes)
        return chromosomes


def convert(chromo):
    pass

if __name__ == "__main__":
    print("Script started as main, please input file to parse.")
    parse_set(input())