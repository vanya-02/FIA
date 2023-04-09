from rules import *
from production import *
from utils import *

possible_facts = [
'(?x) has sunglasses', '(?x) has hawaii t-shirts',
'(?x) stays at a hotel', '(?x) came out of an airport', '(?x) took the first waiting taxi',
'(?x) has accent', '(?x) doesnt speak luna', '(?x) visits museums', '(?x) takes pictures, a LOT of pictures; 10pics/hour',
'(?x) uses a vpn', '(?x) uses public wifi'
]

then_conclusions = [
    '(?x) is Tourist type 1, the broke one',
    '(?x) is Tourist type 2, the cultured one',
    '(?x) Tourist type 3, the foreigner',
    '(?x) is Tourist tytpe 4, the newbie',
    '(?x) is Tourist type 5, the archetype'
]

def extract_strings_within_single_quotes(input_string):
    output_list = []
    start = 0
    while True:
        start_quote = input_string.find("'", start)
        if start_quote == -1:
            break
        end_quote = input_string.find("'", start_quote + 1)
        output_list.append(input_string[start_quote + 1:end_quote])
        start = end_quote + 1
    return output_list

def bw_system(then_conclusions=then_conclusions, possible_facts=None):
    tourist_name = input('Introduce tourist name: ')
    
    print('Possible hypothesis:')
    for i in range(len(then_conclusions)):
        then_conclusions[i] = then_conclusions[i].replace('(?x)', tourist_name)
        print(i, then_conclusions[i])

    # assisgns to varible a possible consequent to verify
    hyposhesis = then_conclusions[int(input('Select hypothesis number to check: '))]
    
    if possible_facts is None:
        bw_chain_to_string = str(backward_chain(TOURIST_RULES, hyposhesis))
        possible_facts = extract_strings_within_single_quotes(bw_chain_to_string)

    
    counter = 0
    print(f'\nPossible facts about {tourist_name}')
    for i in possible_facts:
        facts = i.replace('(?x)', tourist_name)
        print(f"{counter}, {facts}")
        counter += 1
    
    fact_numbers = list(map(int, input('Selects the facts true from above: eg: (2 3 4) \n').split(' ')))

    data = []
    for i in fact_numbers:
        data.append(possible_facts[i])

    result = forward_chain(TOURIST_RULES, data, apply_only_one=True,verbose=False)

    return result





if __name__=='__main__':
    print(bw_system(then_conclusions=then_conclusions, possible_facts=None))


