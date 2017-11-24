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
    pass

def convert(chromo):
    pass

if __name__ == "__main__":
    print("Script started as main, please input file to parse.")
    parse(input())