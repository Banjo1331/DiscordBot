import random
import customGrammar
from nltk.parse.generate import generate
from nltk import CFG
import nltk
from importlib import reload

structures = ['Webapp', 'Bot', 'Desktop App', 'Mobile App']
app_types = ['Machine Learning', 'Natural Language Processing', 'Math Function Plotting', 'Data Visualization',
             'Document Retrieval']
datasets = ['bananas', 'pizza places', 'universities', 'chairs', 'music', 'television', 'geographical', 'historical',
            'clothing', 'public transportation', 'major sports franchise', 'U.S. presidents']


def get_random_string(debug=True):
    if debug == True:
        reload(customGrammar)

    grammar = customGrammar.grammar

    '''structs = "\n  App_Type -> \'"+str(structures[0])+"\'"
    for x in structures[1:]:
        structs +=" | "+"\'"+x+"\'"
    grammar+=structs'''

    '''structs = "\n  Data_Set -> '"+str(datasets[0])+"\'"
    for x in datasets[1:]:
        structs +=" | "+"\'"+x+"\'"
    grammar+=structs'''

    '''structs = "\n  App_Structure -> '"+str(app_types[0])+"\'"
    for x in app_types[1:]:
        structs +=" | "+"\'"+x+"\'"
    grammar+=structs'''

    grammar = CFG.fromstring(grammar)
    count = 0
    sentences = []
    for sentence in generate(grammar):
        sentences.append(str(' '.join(sentence)))
    s = ""

    check = True
    while check:
        s = sentences[random.randint(0, len(sentences))]
        check = False
        for x in structures:
            if s.count(x) == 2:
                check = True
        for x in app_types:
            if s.count(x) == 2:
                check = True
        for x in datasets:
            if s.count(x) == 2:
                check = True

    AT = random.choice(structures)
    s = s.replace("App_Type", AT)

    AS = random.choice(app_types)
    s = s.replace("App_Structure_1", AS)
    if "App_Structure_2" in s:
        AS2 = AS
        while AS2 == AS:
            AS2 = random.choice(app_types)
        s = s.replace("App_Structure_2", AS2)

    data_set_1 = random.choice(datasets)
    s = s.replace("Data_Set_1", data_set_1)
    if "Data_Set_2" in s:
        data_set_2 = data_set_1
        while data_set_2 == data_set_1:
            data_set_2 = random.choice(datasets)
        s = s.replace("Data_Set_2", data_set_2)

    punct = [".", "!"]
    full_string = s + punct[random.randint(0, 1)]
    print(full_string)
    return full_string


def get_keywords(string):
    keywords = []
    for structure in structures:
        if structure in string:
            keywords.append(structure)
    for app_type in app_types:
        if app_type in string:
            keywords.append(app_type)
    return keywords
def main():
    get_random_string(True)
if __name__ == "__main__":
    main()